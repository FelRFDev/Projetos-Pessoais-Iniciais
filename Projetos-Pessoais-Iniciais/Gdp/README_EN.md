<div align="center">

# 🏢 G.D.P — Gatehouse Management System

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

> **A complete terminal-based gatehouse management system — key control, phone extensions, projectors, to-do list, and a built-in voice assistant.**

🇺🇸 You are reading in **English**. | 🇧🇷 [Leia em Português](./README.md)

</div>

---

## 📖 About the Project

**G.D.P (Gestão de Portaria / Gatehouse Management)** is the most complete project in this repository. Developed for real workplace use, it centralizes all daily gatehouse tasks into a single terminal tool: tracking physical keys with assigned numbers, managing a phone extension directory, maintaining a to-do list, controlling projector availability, and recording material charges.

Beyond the manual menu, the system features **Vírtua** — a voice-activated virtual assistant that recognizes commands in Brazilian Portuguese, opens the browser, plays music on YouTube, looks up phone extensions and keys by voice, searches Wikipedia, and much more.

The project has two versions:

| Version | Folder | Highlights |
|---------|--------|------------|
| **v1.0** | `Gdp/` (this folder) | Original stable version |
| **v1.5.1** | `Gdp/Gdp 1.5.1/` | Improved layout with ASCII art banners and menus |

---

## ✨ Main Features

- 🗝️ **Key Control** — Register, remove, edit, and look up physical keys with name and number
- 📞 **Phone Extension Control** — Manage the phone directory for the building
- ✅ **To-Do List** — Daily task agenda for the gatehouse operator
- 📋 **Sector Changes** — Log daily events and changes to the JSON database
- 📽️ **Projector Control** — Track availability of projection equipment
- 💰 **Material Billing** — Record and track charged materials
- 🤖 **Virtual Assistant "Vírtua"** — Recognizes voice commands in PT-BR:
  - 🌐 Open browser and search Google
  - 🎵 Play music on YouTube (`pywhatkit`)
  - 📅 Report the current day and time
  - 📖 Search Wikipedia and read results aloud
  - 😄 Tell jokes
  - 🗝️ Look up phone extensions and keys by voice

---

## 🛠️ Technologies & Tools

| Category           | Technology / Library       | Description                                         |
|--------------------|---------------------------|-----------------------------------------------------|
| **Language**       | Python 3.10+              | Required for `match/case`                           |
| **Persistence**    | `txt` + `json` (built-in) | File-based database using `.txt` and `.json` files  |
| **Reports**        | `python-docx`             | Microsoft Word document generation                  |
| **Progress**       | `tqdm`                    | Visual progress bar                                 |
| **TTS (Speech)**   | `pyttsx3`                 | Text-to-speech conversion (offline)                 |
| **STT (Listen)**   | `SpeechRecognition`       | Voice recognition via Google API                    |
| **Browser**        | `webbrowser` (built-in)   | Opens URLs in the default browser                   |
| **YouTube**        | `pywhatkit`               | Searches and plays music on YouTube                 |
| **Wikipedia**      | `wikipedia`               | Searches and reads Wikipedia articles               |
| **Date/Time**      | `datetime`, `time`        | Day/time info for the assistant                     |

---

## 📂 Architecture & Project Structure

```
Gdp/
│
├── Gdp.py              # Main program — menus and gatehouse logic
├── funcoes.py          # Utility module and Vírtua assistant logic
│
├── chaves.txt          # Key database (created at runtime)
├── nums.txt            # Key number database (created at runtime)
├── NomeRamal.txt       # Extension names database (created at runtime)
├── NumRamal.txt        # Extension numbers database (created at runtime)
├── Afazeres.txt        # To-do list (created at runtime)
├── Alt.json            # Sector change log (created at runtime)
├── Projetores.json     # Projector status (created at runtime)
│
├── requirements.txt    # Project dependencies
├── README.md           # Documentation (Português)
├── README_EN.md        # Documentation (English)
│
└── Gdp 1.5.1/          # Version 1.5.1 — enhanced layout
    ├── Gdp.py
    ├── funcoes.py
    ├── requirements.txt
    ├── README.md
    └── README_EN.md
```

**Modular architecture:**
> `Gdp.py` imports all functions from `funcoes.py` (inside a configurable folder). The folder must be adjusted in the `import` at the top of `Gdp.py`:
> ```python
> from mundo2.funcoes import *   # ← replace "mundo2" with your folder name
> ```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** — [Download](https://www.python.org/downloads/)
- **Microphone** — Required for the Vírtua voice assistant
- **pip** (package manager)

### Step-by-Step

**1. Clone the repository**
```bash
git clone https://github.com/[YOUR_USERNAME]/[REPO_NAME].git
cd "Projetos-Pessoais-Iniciais/Gdp"
```

**2. Place `funcoes.py` inside a subfolder**

Create a folder (e.g., `mundo2`) and move `funcoes.py` into it:
```
Gdp/
└── mundo2/
    └── funcoes.py
```

**3. Update the import in `Gdp.py`**

```python
# Line 1 of Gdp.py — replace the folder name to match yours
from mundo2.funcoes import *
```

**4. Install dependencies**
```bash
pip install -r requirements.txt
```

**5. Run the program**
```bash
python Gdp.py
```

**6. Main menu**
```
----=<<<<<<<<<<<MENU PRINCIPAL>>>>>>>>>>>>=--
1 - ACESSAR MENU
2 - UTILIZAR ASSISTENTE VIRTUAL (VÍRTUA)
3 - SAIR
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

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/felipe-rodrigues-fonseca-843b9421a/)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat-square&logo=gmail)](mailto:comunidadehawks@gmail.com)
