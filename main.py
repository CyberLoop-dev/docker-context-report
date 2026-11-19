import argparse
import fnmatch
import json
from pathlib import Path

def read_patterns(root):
    path = root / ".dockerignore"
    if not path.exists():
        return []
    patterns = []
    for line in path.read_text(encoding="utf-8",errors="replace").splitlines():
        value = line.strip()
        if not value or value.startswith("#") or value == ".":
            continue
        patterns.append(value)
    return patterns

def matches(relative_path, pattern):
    pattern = pattern.lstrip("/")
    directory_only = pattern.endswith("/")
    pattern = pattern.rstrip("/")
    if not pattern:
        return False
    if fnmatch.fnmatch(relative_path,pattern) or fnmatch.fnmatch(Path(relative_path).name,pattern):
        return True
    if directory_only and (relative_path == pattern or relative_path.startswith(pattern + "/")):
        return True
    return False

def is_ignored(relative_path, patterns):
    ignored = False
    for raw in patterns:
        negated = raw.startswith("!")
        pattern = raw[1:] if negated else raw
        if matches(relative_path,pattern):
            ignored = not negated
    return ignored

def analyze(root):
    root = Path(root).resolve()
    patterns = read_patterns(root)
    included, ignored = [], []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(root).as_posix()
        if is_ignored(relative,patterns):
            ignored.append(relative)
        else:
            included.append({"path":relative,"bytes":path.stat().st_size})
    included.sort(key=lambda item:item["bytes"],reverse=True)
    return {"root":str(root),"approximate":True,"included_count":len(included),"ignored_count":len(ignored),
            "total_bytes":sum(item["bytes"] for item in included),"largest":included[:10],"ignored":ignored}

def main():
    parser = argparse.ArgumentParser(description="Preview a Docker build context using common .dockerignore patterns.")
    parser.add_argument("path",type=Path)
    parser.add_argument("--json",action="store_true")
    args = parser.parse_args()
    if not args.path.is_dir():
        parser.error("Build context path must be a directory.")
    result = analyze(args.path)
    if args.json:
        print(json.dumps(result,indent=2))
    else:
        print(f"Approximate context: {result['included_count']} files, {result['total_bytes']} bytes")
        print(f"Ignored: {result['ignored_count']} files")
        for item in result["largest"]:
            print(f"{item['bytes']:>10}  {item['path']}")
        print("\nNote: this implements common patterns, not every Docker matcher edge case.")

if __name__ == "__main__":
    main()
