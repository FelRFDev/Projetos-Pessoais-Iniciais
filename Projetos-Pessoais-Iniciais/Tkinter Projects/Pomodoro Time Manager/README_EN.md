<div align="center">

# 🍅 Pomodoro Time Manager

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational?style=for-the-badge&logo=python)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

> **A Pomodoro timer with a graphical interface, sound alerts, per-cycle images, and instruction/about windows — an enhanced 100 Days of Code exercise.**

🇺🇸 You are reading in **English**. | 🇧🇷 [Leia em Português](./README.md)

</div>

---

## 📖 About the Project

The **Pomodoro Time Manager** is an enhanced version of a *100 Days of Code* exercise. The original version was a basic timer with a label indicating the current cycle. This version expands the idea with **sound alerts** for each cycle transition, **animated images** automatically swapped per phase, an **instructions window** about the Pomodoro technique, and an **About window** with social media links.

### What is the Pomodoro Technique?
Work for **25 minutes** → **5 min** short break → repeat 4 times → **25 min** long break.

---

## ✨ Main Features

- ⏱️ **Full Pomodoro Timer** — Work cycles (25 min), short break (5 min), long break (25 min)
- 🔔 **Sound Alerts** — Distinct sounds on app start, cycle change, and completion
- 🖼️ **Per-Cycle Images** — Different image for each phase (work, short break, long break)
- ✅ **Session Counter** — Checkmarks (✅) accumulate for each completed work session
- ▶️ **Start Button** — Starts the timer and disables itself to prevent double-clicks
- 🔄 **Reset Button** — Cancels the current cycle and resets the counter with a sound
- 📋 **Instructions Screen** — Window explaining how to use the Pomodoro method
- ℹ️ **About Screen** — Window with author info and social media links

---

## 🛠️ Technologies & Tools

| Category        | Technology / Library  | Description                                            |
|-----------------|----------------------|--------------------------------------------------------|
| **Language**    | Python 3.x           | Project's base language                                |
| **GUI**         | `tkinter`            | Graphical interface with Canvas, Button, Label, Toplevel |
| **Audio**       | `pygame` (`mixer`)   | Plays `.mp3` and `.wav` sounds on events               |
| **Browser**     | `webbrowser` (built-in) | Opens external links (author's social media)        |
| **Math**        | `math` (built-in)    | Calculates minutes and seconds for the countdown       |

---

## 📂 Architecture & Project Structure

```
Pomodoro Time Manager/
│
├── main.py                    # Main code with all logic and GUI
│
├── clkbanner.png              # Clock banner displayed at the top
├── tomato.png                 # Tomato image with timer overlay
├── worktime_resized.png       # Work phase image
├── shortbreak_resized.png     # Short break image
├── longbreak_resized.png      # Long break image
├── cape_resized.png           # Background image on start screen
│
├── apito.mp3                  # Cycle alert sound
├── reset.mp3                  # Reset sound
├── jobdone.mp3                # Completion sound
├── start tema.wav             # Timer window opening theme
├── instrucoes tema.wav        # Instructions screen theme
├── tema abertura.wav          # Start screen theme
│
├── requirements.txt           # Project dependencies
├── README.md                  # Documentation (Português)
└── README_EN.md               # Documentation (English)
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** — [Download](https://www.python.org/downloads/)
- **pip** (package manager)
- All image (`.png`, `.jpg`) and audio (`.mp3`, `.wav`) files must be in the **same folder** as `main.py`

### Step-by-Step

**1. Clone the repository**
```bash
git clone https://github.com/[YOUR_USERNAME]/[REPO_NAME].git
cd "Projetos-Pessoais-Iniciais/Tkinter Projects/Pomodoro Time Manager"
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the program**
```bash
python main.py
```

**4. On the start screen:**
- **START** → Opens the Pomodoro timer
- **INSTRUÇÕES** → Explains how to use the Pomodoro method
- **SOBRE O PROGRAMA** → Author information and contacts

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
