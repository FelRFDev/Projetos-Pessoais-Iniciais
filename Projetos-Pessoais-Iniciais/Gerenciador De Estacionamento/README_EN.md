<div align="center">

# 🅿️ Parking Lot Manager

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

> **A terminal-based parking lot management system — control entries, exits, and spot availability in real time.**

🇺🇸 You are reading in **English**. | 🇧🇷 [Leia em Português](./README.md)

</div>

---

## 📖 About the Project

The **Parking Lot Manager** is a Python command-line application for the operational management of a **10-spot** parking lot. The operator can register vehicle entries and exits, check real-time spot availability, and release individual or all spots at once.

This repository contains two versions:

| Version | File | Description |
|---------|------|-------------|
| **v1.0** | `estacionamento.py` (this folder) | Initial functional version |
| **v1.5** | `Gerenciador de Estacionamento 1.5/` | Enhanced version with JSON database, formatted tables, and graphical reports |

---

## ✨ Main Features

- 🕐 **Schedule Registration** — Records driver name, plate, check-in and check-out time per spot
- 🚗 **Spot Release** — Clears a specific spot by name
- 🧹 **Full Release** — Clears all spots at once with a progress bar
- 📊 **Availability View** — Displays the current status of all 10 spots
- 🚪 **Interactive Menu** — Clear navigation with error handling

---

## 🛠️ Technologies & Tools

| Category       | Technology / Library | Description                                    |
|----------------|---------------------|------------------------------------------------|
| **Language**   | Python 3.x          | Project's base language                        |
| **Progress**   | `tqdm`              | Progress bar when releasing all spots          |
| **Time**       | `time` (built-in)   | Pauses and visual feedback in the terminal     |

---

## 📂 Architecture & Project Structure

```
Gerenciador De Estacionamento/
│
├── estacionamento.py                    # v1.0 — initial version
├── requirements.txt                     # v1.0 dependencies
├── README.md                            # Documentation (Português)
├── README_EN.md                         # Documentation (English)
│
└── Gerenciador de Estacionamento 1.5/   # v1.5 — enhanced version
    ├── estacionamento.py                # v1.5 source code
    ├── requirements.txt                 # v1.5 dependencies
    ├── README.md                        # v1.5 docs (PT-BR)
    └── README_EN.md                     # v1.5 docs (EN)
```

> The parking lot is modeled as a **Python dictionary** where each key is a spot (`'vaga 1'` to `'vaga 10'`) and the value is a list with vehicle data. An empty list means the spot is free.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** — [Download](https://www.python.org/downloads/)
- **pip** (package manager)

### Step-by-Step

**1. Clone the repository**
```bash
git clone https://github.com/[YOUR_USERNAME]/[REPO_NAME].git
cd "Projetos-Pessoais-Iniciais/Gerenciador De Estacionamento"
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the program**
```bash
python estacionamento.py
```

**4. Navigate the menu**
```
<< MENU INICIAL >>

[1] - Cadastrar horário
[2] - Liberar vaga
[3] - Liberar todas as vagas
[4] - Disponibilidade das Vagas
[5] - Sair
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
