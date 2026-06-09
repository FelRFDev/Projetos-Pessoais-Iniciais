<div align="center">

# 🧠 Be Wise — Assistente Desktop com IA Local

[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-9b59b6?style=for-the-badge&logo=python)](https://github.com/TomSchimansky/CustomTkinter)
[![GPT4All](https://img.shields.io/badge/IA-GPT4All%20(Offline)-orange?style=for-the-badge)](https://github.com/nomic-ai/gpt4all)
[![License](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)](./LICENSE)

> **Aplicação desktop com IA generativa rodando 100% offline via GPT4All — pesquise, gere áudios, exporte para Word e extraia texto de imagens, tudo sem internet.**

🇧🇷 Você está lendo em **Português**. | 🇺🇸 [Read in English](./README_EN.md)

</div>

---

## 📖 Sobre o Projeto

O **Be Wise** é uma aplicação desktop com interface gráfica moderna desenvolvida com **CustomTkinter**, que utiliza o **GPT4All** para executar um modelo de linguagem de grande escala (LLM) diretamente na máquina do usuário, **sem necessidade de conexão com a internet ou chave de API**.

O projeto foi concebido para ser um conjunto de ferramentas inteligentes para o dia a dia: fazer perguntas a uma IA local, converter respostas em arquivos de áudio `.mp3`, exportar o conteúdo para documentos Word `.docx`, criar diretórios de organização e extrair texto de imagens com OCR.

---

## ✨ Funcionalidades Principais

- 🤖 **IA Generativa Offline** — Executa o modelo `Meta-Llama-3-8B-Instruct.Q4_0.gguf` via GPT4All, sem internet
- 🔊 **Geração de Áudio** — Converte o texto da resposta em arquivo de áudio `.mp3` via `pyttsx3`
- 📝 **Exportação para Word** — Salva a resposta como arquivo `.docx` formatado
- 📁 **Criação de Diretórios** — Cria pastas de organização via diálogo de seleção
- 🖼️ **Extração de Texto de Imagem (OCR)** — Transforma imagens `jpg/png/gif` em documentos `.docx` via `pytesseract`
- ✏️ **Campo de Resposta Editável** — O usuário pode editar o texto gerado antes de exportar

---

## 🛠️ Tecnologias e Ferramentas

| Categoria        | Tecnologia / Biblioteca  | Descrição                                              |
|------------------|-------------------------|--------------------------------------------------------|
| **Linguagem**    | Python 3.x              | Linguagem base do projeto                              |
| **GUI**          | `customtkinter`         | Interface gráfica moderna com tema escuro/claro        |
| **IA Local**     | `gpt4all`               | LLM rodando 100% offline na máquina do usuário         |
| **TTS (Fala)**   | `pyttsx3`               | Converte texto em áudio `.mp3` (offline)               |
| **OCR**          | `pytesseract`           | Extração de texto de imagens (requer Tesseract-OCR)    |
| **Word**         | `python-docx`           | Criação de documentos `.docx` com o conteúdo gerado    |
| **HTTP**         | `requests`              | Requisições HTTP (infraestrutura futura)               |
| **Dados**        | `base64` (built-in)     | Codificação de imagens embarcadas na GUI               |

---

## 📂 Estrutura do Projeto

```
be_wise/
│
├── bewise.py              # Arquivo principal — inicia a GUI
├── bw_funcoes.py          # Módulo com toda a lógica de funcionalidades
├── b64_imgs.py            # Imagens da GUI codificadas em Base64
│
├── project_settings/      # Configurações do ambiente (Poetry)
│   ├── pyproject.toml     # Dependências gerenciadas pelo Poetry
│   └── .venv/             # Ambiente virtual (criado pelo Poetry)
│
├── requirements.txt       # Dependências alternativas (pip)
├── readme.md              # Documentação (Português)
└── README_EN.md           # Documentação (English)
```

> **Importante:** O `pytesseract` requer a instalação separada do [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki) no sistema. O caminho padrão configurado é `C:\Program Files\Tesseract-OCR\tesseract.exe`.

---

## 🚀 Como Começar

### Pré-requisitos

- **Python 3.10+** — [Download](https://www.python.org/downloads/)
- **Tesseract-OCR** (para OCR) — [Download para Windows](https://github.com/UB-Mannheim/tesseract/wiki)
- **pip** ou **Poetry** (gerenciador de pacotes)

### Instalação com pip

**1. Clone o repositório**
```bash
git clone https://github.com/[SEU_USUARIO]/[NOME_DO_REPO].git
cd "Projetos-Pessoais-Iniciais/Tkinter Projects/be_wise"
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Execute o programa**
```bash
python bewise.py
```

### Instalação com Poetry *(recomendado)*

```bash
pip install poetry
cd project_settings
poetry shell       # Cria e ativa a venv na 1ª vez
poetry install     # Instala as dependências do pyproject.toml
cd ..
python bewise.py
```

### Download do Modelo de IA

O modelo `Meta-Llama-3-8B-Instruct.Q4_0.gguf` (~4 GB) será baixado automaticamente pelo GPT4All na primeira execução. Certifique-se de ter espaço suficiente em disco.

---

## 🤝 Como Contribuir

1. Faça um **Fork** do projeto
2. Crie uma branch para sua feature: `git checkout -b feature/minha-feature`
3. Faça suas alterações e commit: `git commit -m 'feat: adiciona minha feature'`
4. Envie para a branch: `git push origin feature/minha-feature`
5. Abra um **Pull Request**

---

## 📝 Licença e Contato

Este projeto está licenciado sob a **Licença MIT**. Consulte o arquivo `LICENSE` para mais detalhes.

**Autor:** Felipe Rodrigues Fonseca

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/felipe-rodrigues-fonseca-843b9421a/)
[![E-mail](https://img.shields.io/badge/E--mail-Contato-red?style=flat-square&logo=gmail)](mailto:comunidadehawks@gmail.com)
