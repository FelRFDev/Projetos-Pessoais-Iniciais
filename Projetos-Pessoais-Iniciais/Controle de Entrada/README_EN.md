<div align="center">

# 📋 Entry Control System

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

> **A terminal-based gatehouse system for registering and controlling visitor entries and exits, with automated daily report delivery via email.**

🇺🇸 You are reading in **English**. | 🇧🇷 [Leia em Português](./README.md)

</div>

---

## 📖 About the Project

**Entry Control System** is a Python command-line application designed for use in gatehouses and reception desks. It solves the problem of manually tracking visitor entries and exits by centralizing all data in a local JSON database and automatically sending a daily report by email at the end of the shift.

The project ships in two versions:
- **`ControleDeEntradaTXT.py`** — Generates reports as plain `.txt` files
- **`ControledeEntradaWord.py`** — Generates formatted table reports as `.docx` (Microsoft Word) files

---

## ✨ Main Features

- 📝 **Entry Registration** — Records visitor name, vehicle plate, and check-in time
- 🚪 **Exit Registration** — Logs check-out time by visitor name
- 🔍 **Record Query** — Displays all daily records formatted in the terminal
- ✏️ **Data Editing** — Allows correcting a visitor's name after registration
- 🗑️ **Record Clearing** — Wipes all records with a safety confirmation prompt
- 📧 **Email Report** — Generates a report file and sends it as an email attachment via SMTP (Gmail)
- 📄 **Word Export** — *(Word version)* Exports data into a formatted table in a `.docx` file

---

## 🛠️ Technologies & Tools

| Category        | Technology / Library          | Description                                   |
|-----------------|-------------------------------|-----------------------------------------------|
| **Language**    | Python 3.x                    | Project's base language                       |
| **Persistence** | `json` (built-in)             | Local database stored as a `.json` file       |
| **Email**       | `smtplib`, `email` (built-in) | Sending emails with attachments via SMTP      |
| **Progress**    | `tqdm`                        | Visual progress bar in the terminal           |
| **Time**        | `datetime`, `time` (built-in) | Date control and execution pauses             |
| **Word**        | `python-docx`                 | Report generation in `.docx` *(Word version)* |

---

## 📂 Architecture & Project Structure

```
Controle de Entrada/
│
├── ControleDeEntradaTXT.py    # Version with .txt report and email delivery
├── ControledeEntradaWord.py   # Version with formatted .docx table report
├── bd.json                    # Local database (created at runtime)
├── registro.txt               # Auxiliary registration file (created at runtime)
├── requirements.txt           # Project dependencies
├── README.md                  # Documentation (Português)
└── README_EN.md               # Documentation (English)
```

> The `bd.json` file centralizes all visitor records. The `BancoDados` class handles database creation, while `bdFuncoes` encapsulates data manipulation (CRUD operations).

---

## 🚀 Getting Started

### Prerequisites

Make sure you have installed:

- **Python 3.8+** — [Download](https://www.python.org/downloads/)
- **pip** (package manager, bundled with Python)

### Step-by-Step

**1. Clone the repository**
```bash
git clone https://github.com/[YOUR_USERNAME]/[REPO_NAME].git
cd "Projetos-Pessoais-Iniciais/Controle de Entrada"
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure email credentials**

Before running, open the `.py` file you want to use and fill in the email variables:
```python
fromaddr = "[YOUR_EMAIL@gmail.com]"          # Sender email address
toaddr   = "[RECIPIENT_EMAIL@...]"           # Recipient email address
# ...
server.login(fromaddr, "[YOUR_GMAIL_APP_PASSWORD]")
```
> ⚠️ It is strongly recommended to use a **Gmail App Password** instead of your main account password. Generate one at: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

**4. Run the program**

For the `.txt` report version:
```bash
python ControleDeEntradaTXT.py
```

For the `.docx` report version:
```bash
python ControledeEntradaWord.py
```

---

## 🤝 How to Contribute

1. **Fork** the project
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'feat: add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a **Pull Request**

---

## 📝 License & Contact

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

**Author:** Felipe Rodrigues Fonseca

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)]([YOUR_LINKEDIN])
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat-square&logo=gmail)](mailto:[YOUR_EMAIL])
