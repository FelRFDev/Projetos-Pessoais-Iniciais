<div align="center">

# 🔑 My Pass — Password Manager

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational?style=for-the-badge&logo=python)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

> **A GUI password manager (Tkinter) with per-user login, a customizable password generator, Treeview table visualization with password masking — 100% local storage.**

🇺🇸 You are reading in **English**. | 🇧🇷 [Leia em Português](./README.md)

</div>

---

## 📖 About the Project

**My Pass** is an expanded and improved version of a *100 Days of Code* exercise. While the original exercise was a simple window for saving passwords to a `.txt` file, this version evolved into a full-featured manager with a **per-user login system**, **customizable password generator**, **Treeview table visualization**, and **`.txt` export**.

Each user gets their own isolated folder with a dedicated JSON database, ensuring no user's data is accessible to another.

---

## ✨ Main Features

- 👤 **Register & Login** — Built-in authentication; each user gets an individual folder with their data
- 🔑 **Password Registration** — Saves Website, Username, and Password to `websites.json`
- 🎲 **Password Generator** — Creates complex passwords with options: uppercase, lowercase, numbers, symbols
- 📋 **Domain Auto-fill** — Listbox with common domains (`@gmail.com`, `@outlook.com`...) for the email field
- 🔍 **Table Visualization** — Displays all entries in a `ttk.Treeview` with a scrollbar
- 👁️ **Hide/Show Passwords** — Toggles between asterisks and real password with a single click
- 🗑️ **Individual Removal** — Removes a specific entry by website name
- 🧹 **Clear All** — Wipes all data with a safety confirmation
- 📄 **TXT Export** — Automatically generates a `.txt` backup file in the user's folder
- 📁 **Clipboard Copy** — Generated password is automatically copied with `pyperclip`

---

## 🛠️ Technologies & Tools

| Category         | Technology / Library   | Description                                            |
|------------------|------------------------|--------------------------------------------------------|
| **Language**     | Python 3.x             | Project's base language                                |
| **GUI**          | `tkinter` + `ttk`      | Graphical interface, windows, Treeview and Scrollbar   |
| **Persistence**  | `json` (built-in)      | Per-user local database in `.json` files               |
| **Clipboard**    | `pyperclip`            | Copies generated password to clipboard                 |
| **Randomness**   | `random` (built-in)    | Random password generation                             |
| **System**       | `os` (built-in)        | Per-user directory creation                            |

---

## 📂 Architecture & Project Structure

```
My Pass/
│
├── main.py               # Main code with all logic and GUI
├── logo.png              # Logo shown in the password window
├── cadastro.png          # Registration screen image
├── lp.png                # Mini logo in the main window
├── lg2.png               # Image in the management window
├── blueeye_resized.png   # Icon for the hide/show passwords button
│
├── users_data/           # Folder created at runtime
│   └── [username]/       # Individual folder per user
│       ├── usuarios_bd.json   # User login credentials
│       ├── websites.json      # Saved passwords
│       └── dados.txt          # Exported .txt backup
│
├── requirements.txt      # Project dependencies
├── README.md             # Documentation (Português)
└── README_EN.md          # Documentation (English)
```

> **Per-user isolation architecture:** The `cria_dir_user()` function automatically creates a subfolder named after the user inside `users_data/` on first access, guaranteeing full data separation.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** — [Download](https://www.python.org/downloads/)
- **pip** (package manager)
- Image files (`.png`) must be in the **same folder** as `main.py`

### Step-by-Step

**1. Clone the repository**
```bash
git clone https://github.com/[YOUR_USERNAME]/[REPO_NAME].git
cd "Projetos-Pessoais-Iniciais/Tkinter Projects/My Pass"
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the program**
```bash
python main.py
```

**4. Create your account**
- On the start screen, click **CADASTRAR** and choose a username and password
- After registration, log in to access the password manager

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

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/felipe-rodrigues-fonseca-843b9421a/)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat-square&logo=gmail)](mailto:comunidadehawks@gmail.com)
