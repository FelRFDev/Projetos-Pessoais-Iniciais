<div align="center">

# 🎯 Number Guessing Game

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

> **An interactive terminal game where the player has 3 lives to guess a computer-generated number — featuring dynamic ASCII art and real-time visual feedback.**

🇺🇸 You are reading in **English**. | 🇧🇷 [Leia em Português](./README.md)

</div>

---

## 📖 About the Project

The **Number Guessing Game** is a simple terminal game built in Python to practice programming logic, conditional structures, and dictionary manipulation. Each round, the computer draws a random number between 1 and 10, and the player has **3 lives** to guess it correctly.

The highlight of the project is its visual feedback system: with each life lost, a heart-shaped ASCII art display shrinks in real time in the terminal, creating an immersive experience even without a graphical interface.

---

## ✨ Main Features

- 🎲 **Random Draw** — Number generated with `random.randint` at the start of each game
- ❤️ **Life System** — Player starts with 3 lives, displayed as dynamic ASCII art hearts
- 🖥️ **Terminal Visual Feedback** — ASCII heart art shrinks as lives are lost
- 🏆 **Win Condition** — Displays a trophy in ASCII art when the correct number is guessed
- 💀 **Game Over** — Clear message when all attempts are exhausted
- 🧑 **Personalization** — The game asks for the player's name and uses it throughout

---

## 🛠️ Technologies & Tools

| Category          | Technology / Library | Description                               |
|-------------------|---------------------|-------------------------------------------|
| **Language**      | Python 3.x          | Project's base language                   |
| **Randomness**    | `random` (built-in) | Draws the number to be guessed            |

> ✅ No external dependencies. The project runs with a standard Python installation.

---

## 📂 Architecture & Project Structure

```
jogo_adivinhacao/
│
├── main.py         # Main file with all game logic
├── README.md       # Documentation (Português)
└── README_EN.md    # Documentation (English)
```

**Program flow:**
- `player_lifes_stages` — Dictionary mapping remaining lives (3, 2, 1) to their ASCII art representation
- `numero_sorteado` — Random number generated once per game session
- Main loop — Receives the player's guess, compares it to the drawn number, and decides game state

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** — [Download](https://www.python.org/downloads/)

### Step-by-Step

**1. Clone the repository**
```bash
git clone https://github.com/[YOUR_USERNAME]/[REPO_NAME].git
cd "Projetos-Pessoais-Iniciais/jogo_adivinhacao"
```

**2. Install dependencies**

This project only uses Python's built-in `random` library. No additional installation required.

**3. Run the game**
```bash
python main.py
```

**4. Play!**
```
Informe o seu nome: Felipe

██╗   ██╗██╗██████╗  █████╗ ███████╗
...
,-.-. ,-.-. ,-.-. 
`. ,' `. ,' `. ,'
  `     `     `

Bem vindo ao jogo de adivinhação Felipe!
Mostre que você é fera e adivinhe o número sorteado pelo computador.

Digite um número: _
```

---

## 🤝 How to Contribute

1. **Fork** the project
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'feat: add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a **Pull Request**

**Suggested improvements:**
- 🎯 Add "hot/cold" hints (higher/lower)
- 🏅 Scoring system and leaderboard
- 🔄 Option to play again without restarting the script
- 🎨 Add terminal colors using `colorama`

---

## 📝 License & Contact

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

**Author:** Felipe Rodrigues Fonseca

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)]([YOUR_LINKEDIN])
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat-square&logo=gmail)](mailto:[YOUR_EMAIL])
