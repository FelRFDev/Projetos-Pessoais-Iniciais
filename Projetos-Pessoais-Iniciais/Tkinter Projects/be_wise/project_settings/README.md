<div align="center">

# ⚙️ project-settings — Configurações do Ambiente Be Wise

[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)](.)
[![Poetry](https://img.shields.io/badge/Gerenciador-Poetry-blue?style=for-the-badge&logo=poetry&logoColor=white)](https://python-poetry.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)](../LICENSE)

> **Gerenciador de ambiente virtual e controle de dependências para o assistente local Be Wise utilizando Poetry.**

🇧🇷 Você está lendo em **Português**. | 🇺🇸 [Read in English](./README_EN.md)

</div>

---

## 📖 Sobre o Projeto

O **project-settings** é a pasta de gerenciamento de ambiente virtual e dependências da aplicação **Be Wise** (assistente local com IA offline). Este subprojeto foi estruturado utilizando o **Poetry**, um gerenciador de dependências moderno para Python, garantindo uma instalação determinística, isolada e livre de conflitos de pacotes.

A pasta centraliza todas as configurações necessárias para inicializar, testar e empacotar o projeto principal de forma padronizada.

---

## ✨ Funcionalidades Principais

- 📦 **Gerenciamento com Poetry** — Resolução inteligente de dependências através dos arquivos `pyproject.toml` e `poetry.lock`.
- 🔒 **Ambiente Isolado** — Criação de um ambiente virtual (`.venv`) dedicado apenas a esta aplicação.
- 📋 **Compatibilidade Pip** — Disponibilização de um arquivo `requirements.txt` atualizado para instalações tradicionais.
- 🧪 **Preparação para Testes** — Suporte inicial estruturado para testes automatizados.

---

## 🛠️ Tecnologias e Ferramentas

| Categoria | Tecnologia / Ferramenta | Descrição |
| :--- | :--- | :--- |
| **Gerenciador** | Poetry | Resolução e controle de pacotes Python |
| **Linguagem** | Python 3.10+ | Linguagem base do projeto |
| **Dependências** | pyproject.toml | Arquivo de metadados e dependências declaradas |
| **Lockfile** | poetry.lock | Registro com versões exatas das dependências instaladas |

---

## 📂 Estrutura do Projeto

```
project_settings/
│
├── project_settings/
│   └── __init__.py      # Módulo inicializado do Poetry
│
├── tests/
│   └── __init__.py      # Inicialização de testes automatizados
│
├── poetry.lock          # Registro das versões exatas instaladas
├── pyproject.toml       # Dependências e configurações do Poetry
├── requirements.txt     # Dependências para instalação via pip tradicional
├── README.md            # Esta documentação (Português)
└── README_EN.md         # Documentação (English)
```

---

## 🚀 Como Começar

### Pré-requisitos

Antes de configurar o ambiente, certifique-se de ter instalado:
* **Python 3.10+**
* **Poetry** (Instale via pip caso não possua: `pip install poetry`)

### Passo a Passo de Instalação e Execução

**1. Acesse o diretório de configurações**
```bash
cd "Projetos-Pessoais-Iniciais/Tkinter Projects/be_wise/project_settings"
```

**2. Instale as dependências com o Poetry**
```bash
poetry install
```
*Este comando irá criar o ambiente virtual (`.venv`) e instalar todas as bibliotecas necessárias automaticamente.*

**3. Ative o ambiente virtual**
```bash
poetry shell
```

**4. Execute o Be Wise através do ambiente Poetry**
```bash
cd ..
python bewise.py
```

---

## 🤝 Como Contribuir

1. Faça um **Fork** do projeto.
2. Crie uma branch para sua feature: `git checkout -b feature/sua-feature`.
3. Faça commit de suas alterações: `git commit -m 'feat: adiciona nova feature'`.
4. Envie para o repositório remoto: `git push origin feature/sua-feature`.
5. Abra um **Pull Request**.

---

## 📝 Licença e Contato

Este projeto está licenciado sob a **Licença MIT**.

**Autor:** Felipe Rodrigues Fonseca

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/felipe-rodrigues-fonseca-843b9421a/)
[![E-mail](https://img.shields.io/badge/E--mail-Contato-red?style=flat-square&logo=gmail)](mailto:comunidadehawks@gmail.com)
