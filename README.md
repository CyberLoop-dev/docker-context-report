<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:0f766e&height=170&section=header&text=Docker%20Context%20Report&fontColor=ffffff&fontSize=34" alt="Docker Context Report banner"/></p>
<p align="center"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=19&duration=2800&pause=900&center=true&vCenter=true&width=620&lines=Preview%20your%20Docker%20context%3BUnderstand%20ignored%20files%3BEstimate%20build%20payload%20size" alt="Typing title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/docker-context-report?style=flat-square"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/docker-context-report?style=flat-square"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/docker-context-report?style=flat-square"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/docker-context-report?style=flat-square"/></p>
<p align="center"><img src="assets/mark.svg" width="520" alt="Docker Context Report illustration"/></p>

## 🧭 Overview
Docker Context Report walks a local build directory and estimates which files are included after applying common `.dockerignore` patterns. It is a read-only preview and clearly labels its matching rules as an approximation.

## ✨ Features
- 📦 Count included files and estimate total bytes
- 🚫 Apply common glob, directory, and negation rules from `.dockerignore`
- 📊 Show the largest files likely to enter the build context
- 🔒 Never builds an image or changes the source directory

## 🖥️ Demo
No hosted demo is provided. Run the project locally using the quick-start command.

## 🚀 Quick Start
Requires Python 3.10 or newer.

```bash
python main.py ./app
```

Run checks with `python -m unittest discover -s tests -v`.

## 🧰 Tech Stack
- Python standard library
- `argparse` CLI and `unittest`
- Read-only inspection by default

## 🗂️ Folder Structure
```text
.
├── .github/workflows/ci.yml
├── assets/mark.svg
├── tests/test_main.py
├── main.py
├── pyproject.toml
└── README.md
```

## 🗺️ Roadmap
- [ ] Add more edge-case fixtures
- [ ] Improve machine-readable output
- [ ] Keep the core workflow lightweight and local-first

## 🤝 Contributing
Issues and focused pull requests are welcome. Add regression tests for parser and reporting changes.

## 📄 License
MIT License. See [LICENSE](LICENSE).
<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:0f172a&height=100&section=footer" alt="Animated wave footer"/></p>
