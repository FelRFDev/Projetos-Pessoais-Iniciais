<div align="center">

# ⚙️ project-settings — Be Wise Environment Settings

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)](.)
[![Poetry](https://img.shields.io/badge/Manager-Poetry-blue?style=for-the-badge&logo=poetry&logoColor=white)](https://python-poetry.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](../LICENSE)

> **Virtual environment manager and dependency control for the Be Wise local AI desktop assistant using Poetry.**

🇺🇸 You are reading in **English**. | 🇧🇷 [Leia em Português](./README.md)

</div>

---

## 📖 About the Project

**project-settings** is the virtual environment and dependency management folder for the **Be Wise** application (an offline local AI assistant). This subproject was structured using **Poetry**, a modern dependency manager for Python, ensuring a deterministic, isolated, and conflict-free package installation.

This directory centralizes all configurations required to initialize, test, and package the main project in a standardized way.

---

## ✨ Main Features

- 📦 **Poetry Management** — Smart dependency resolution using `pyproject.toml` and `poetry.lock`.
- 🔒 **Isolated Environment** — Automatic creation of a dedicated virtual environment (`.venv`) to prevent conflicts with global Python packages.
- 📋 **Pip Compatibility** — An updated `requirements.txt` file is provided for traditional pip installations.
- 🧪 **Test Readiness** — Structured initial setup for automated tests.

---

## 🛠️ Technologies and Tools

| Category | Technology / Tool | Description |
| :--- | :--- | :--- |
| **Manager** | Poetry | Python package control and resolution |
| **Language** | Python 3.10+ | Base language of the project |
| **Dependencies** | pyproject.toml | Metadata and declared dependencies file |
| **Lockfile** | poetry.lock | Log with exact versions of installed dependencies |

---

## 📂 Project Structure

```
project_settings/
│
├── project_settings/
│   └── __init__.py      # Initialized Poetry module
│
├── tests/
│   └── __init__.py      # Initialization of automated tests
│
├── poetry.lock          # Register of the exact installed versions
├── pyproject.toml       # Poetry dependencies and settings
├── requirements.txt     # Dependencies for traditional pip installation
├── README.md            # Portuguese documentation
└── README_EN.md         # This documentation (English)
```

---

## 🚀 Getting Started

### Prerequisites

Before setting up the environment, make sure you have installed:
* **Python 3.10+**
* **Poetry** (Install via pip if you don't have it: `pip install poetry`)

### Step-by-Step Installation and Execution

**1. Access the configuration directory**
```bash
cd "Projetos-Pessoais-Iniciais/Tkinter Projects/be_wise/project_settings"
```

**2. Install dependencies with Poetry**
```bash
poetry install
```
*This command will automatically create the virtual environment (`.venv`) and install all required libraries.*

**3. Activate the virtual environment**
```bash
poetry shell
```

**4. Run Be Wise through the Poetry environment**
```bash
cd ..
python bewise.py
```

---

## 🤝 How to Contribute

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'feat: add new feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a Pull Request.

---

## 📝 License and Contact

This project is licensed under the **MIT License**.

**Author:** Felipe Rodrigues Fonseca

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/felipe-rodrigues-fonseca-843b9421a/)
[![E-mail](https://img.shields.io/badge/E--mail-Contact-red?style=flat-square&logo=gmail)](mailto:comunidadehawks@gmail.com)
