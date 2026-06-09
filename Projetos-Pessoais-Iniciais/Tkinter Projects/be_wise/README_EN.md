<div align="center">

# 🧠 Be Wise — Local AI Desktop Assistant

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-9b59b6?style=for-the-badge&logo=python)](https://github.com/TomSchimansky/CustomTkinter)
[![GPT4All](https://img.shields.io/badge/AI-GPT4All%20(Offline)-orange?style=for-the-badge)](https://github.com/nomic-ai/gpt4all)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

> **A desktop application with 100% offline generative AI via GPT4All — search, generate audio, export to Word, and extract text from images, all without internet.**

🇺🇸 You are reading in **English**. | 🇧🇷 [Leia em Português](./README.md)

</div>

---

## 📖 About the Project

**Be Wise** is a modern desktop application with a graphical interface built with **CustomTkinter**, powered by **GPT4All** to run a large language model (LLM) directly on the user's machine — **no internet connection or API key required**.

The project was designed as a set of intelligent daily-use tools: ask questions to a local AI, convert responses into `.mp3` audio files, export content to `.docx` Word documents, create organization folders, and extract text from images using OCR.

---

## ✨ Main Features

- 🤖 **Offline Generative AI** — Runs `Meta-Llama-3-8B-Instruct.Q4_0.gguf` via GPT4All, no internet needed
- 🔊 **Audio Generation** — Converts the AI response text into an `.mp3` audio file via `pyttsx3`
- 📝 **Word Export** — Saves the response as a formatted `.docx` file
- 📁 **Directory Creation** — Creates organization folders via a save dialog
- 🖼️ **Image-to-Text (OCR)** — Converts `jpg/png/gif` images into `.docx` documents via `pytesseract`
- ✏️ **Editable Response Field** — The user can edit the generated text before exporting

---

## 🛠️ Technologies & Tools

| Category         | Technology / Library   | Description                                            |
|------------------|------------------------|--------------------------------------------------------|
| **Language**     | Python 3.x             | Project's base language                                |
| **GUI**          | `customtkinter`        | Modern GUI with dark/light theme support               |
| **Local AI**     | `gpt4all`              | LLM running 100% offline on the user's machine         |
| **TTS (Speech)** | `pyttsx3`              | Text-to-audio `.mp3` conversion (offline)              |
| **OCR**          | `pytesseract`          | Text extraction from images (requires Tesseract-OCR)   |
| **Word**         | `python-docx`          | Creates `.docx` documents with generated content       |
| **HTTP**         | `requests`             | HTTP requests (future infrastructure)                  |
| **Data**         | `base64` (built-in)    | Encodes embedded GUI images                            |

---

## 📂 Architecture & Project Structure

```
be_wise/
│
├── bewise.py              # Main file — launches the GUI
├── bw_funcoes.py          # Module with all feature logic
├── b64_imgs.py            # GUI images encoded in Base64
│
├── project_settings/      # Environment settings (Poetry)
│   ├── pyproject.toml     # Poetry-managed dependencies
│   └── .venv/             # Virtual environment (created by Poetry)
│
├── requirements.txt       # Alternative dependencies (pip)
├── readme.md              # Documentation (Português)
└── README_EN.md           # Documentation (English)
```

> **Important:** `pytesseract` requires a separate installation of [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki). The default configured path is `C:\Program Files\Tesseract-OCR\tesseract.exe`.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** — [Download](https://www.python.org/downloads/)
- **Tesseract-OCR** (for OCR) — [Windows Download](https://github.com/UB-Mannheim/tesseract/wiki)
- **pip** or **Poetry**

### Installation with pip

**1. Clone the repository**
```bash
git clone https://github.com/[YOUR_USERNAME]/[REPO_NAME].git
cd "Projetos-Pessoais-Iniciais/Tkinter Projects/be_wise"
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the program**
```bash
python bewise.py
```

### Installation with Poetry *(recommended)*

```bash
pip install poetry
cd project_settings
poetry shell       # Creates and activates the venv on first run
poetry install     # Installs dependencies from pyproject.toml
cd ..
python bewise.py
```

### AI Model Download

The `Meta-Llama-3-8B-Instruct.Q4_0.gguf` model (~4 GB) will be downloaded automatically by GPT4All on first run. Make sure you have enough disk space.

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
