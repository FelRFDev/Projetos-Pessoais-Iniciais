<div align="center">

# 🔐 Login System

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

> **A terminal-based authentication system featuring registration, login, password recovery, and password change — with JSON persistence and email notifications.**

🇺🇸 You are reading in **English**. | 🇧🇷 [Leia em Português](./README.md)

</div>

---

## 📖 About the Project

The **Login System** is a command-line application that implements a complete user authentication flow without relying on any external framework or database engine. All data is stored in a local `.json` file, making the project fully portable.

It was built as a reusable module: the code block marked `#BLOCO PARA INSERIR O PROGRAMA DESEJADO` allows any other application to be "anchored" after a successful login, turning this system into a plug-and-play authentication layer.

---

## ✨ Main Features

- 👤 **Registration** — Records full name, email (used as username), and password
- 🔑 **Login with Attempt Limit** — Locks out after 5 incorrect username or password attempts
- 📧 **Access Recovery** — Sends login credentials to the registered email address via SMTP
- 🔒 **Password Change** — Allows resetting the password with validation against the old one
- 💾 **Local Persistence** — All data saved in `usuarios.json` — no external database required

---

## 🛠️ Technologies & Tools

| Category        | Technology / Library          | Description                                      |
|-----------------|-------------------------------|--------------------------------------------------|
| **Language**    | Python 3.x                    | Project's base language                          |
| **Persistence** | `json` (built-in)             | Local user storage in a `.json` file             |
| **Email**       | `smtplib`, `email` (built-in) | Recovery email delivery via SMTP (Gmail)         |
| **Date**        | `datetime` (built-in)         | Timestamp in the email body                      |
| **Time**        | `time` (built-in)             | Pauses and visual terminal feedback              |

---

## 📂 Architecture & Project Structure

```
Sistema de Login/
│
├── LoginSystem.py      # Main file with all authentication logic
├── usuarios.json       # Local database (created at runtime)
├── requirements.txt    # Project dependencies (stdlib only)
├── README.md           # Documentation (Português)
└── README_EN.md        # Documentation (English)
```

> The `CriaBD()` function is called at startup and ensures `usuarios.json` is created if it doesn't exist. Each user is stored as a `[name, email, password]` list inside a main list.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** — [Download](https://www.python.org/downloads/)

### Step-by-Step

**1. Clone the repository**
```bash
git clone https://github.com/[YOUR_USERNAME]/[REPO_NAME].git
cd "Projetos-Pessoais-Iniciais/Sistema de Login"
```

**2. Install dependencies**

This project uses only Python's standard library. No additional installation required.

**3. Configure email recovery**

Open `LoginSystem.py` and fill in the variables inside the `EnviaEmail` function:
```python
fromaddr = "[YOUR_EMAIL@gmail.com]"   # Sender email (account that sends recovery emails)
# Login credentials also need to be set:
server.login(fromaddr, "[YOUR_GMAIL_APP_PASSWORD]")
```
> ⚠️ Use a **Gmail App Password**, not your main account password. Generate one at: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

**4. Run the program**
```bash
python LoginSystem.py
```

**5. Navigate the menu**
```
>>>>>>>  ACCESS AREA <<<<<<<<

[1] - Register
[2] - Log in
[3] - Recover Access
[4] - Change Password
[5] - Exit
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
