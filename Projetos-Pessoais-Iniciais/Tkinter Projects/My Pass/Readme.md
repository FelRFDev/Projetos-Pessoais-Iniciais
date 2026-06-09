<div align="center">

# 🔑 My Pass — Gerenciador de Senhas

[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational?style=for-the-badge&logo=python)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)](./LICENSE)

> **Gerenciador de senhas com interface gráfica (Tkinter), sistema de login por usuário, gerador de senhas e visualização em tabela com ocultação — armazenamento 100% local.**

🇧🇷 Você está lendo em **Português**. | 🇺🇸 [Read in English](./README_EN.md)

</div>

---

## 📖 Sobre o Projeto

O **My Pass** é uma versão expandida e aprimorada de um exercício do curso *100 Days of Code*. Enquanto o exercício original era uma janela simples para salvar senhas em `.txt`, esta versão evoluiu para um gerenciador completo com **sistema de login por usuário**, **gerador de senhas personalizável**, **visualização em tabela com Treeview**, e **exportação para `.txt`**.

Cada usuário tem sua própria pasta isolada com banco de dados JSON dedicado, garantindo que nenhuma informação de um usuário seja acessível a outro.

---

## ✨ Funcionalidades Principais

- 👤 **Cadastro e Login** — Sistema de autenticação próprio; cada usuário tem uma pasta individual com seus dados
- 🔑 **Cadastro de Senhas** — Salva Website, Usuário e Senha em `websites.json`
- 🎲 **Gerador de Senhas** — Cria senhas complexas com opções de: letras maiúsculas, minúsculas, números e símbolos
- 📋 **Auto-preenchimento de Domínio** — Listbox com domínios comuns (`@gmail.com`, `@outlook.com`...) para o campo e-mail
- 🔍 **Visualização em Tabela** — Exibe todos os cadastros em `ttk.Treeview` com barra de rolagem
- 👁️ **Ocultar/Exibir Senhas** — Alterna entre asteriscos e senha real com um clique
- 🗑️ **Remoção Individual** — Remove um cadastro específico por nome do website
- 🧹 **Limpar Cadastro** — Apaga todos os dados com confirmação de segurança
- 📄 **Exportação para TXT** — Gera automaticamente um arquivo `.txt` de backup na pasta do usuário
- 📁 **Copiar para Área de Transferência** — Senha gerada é copiada automaticamente com `pyperclip`

---

## 🛠️ Tecnologias e Ferramentas

| Categoria        | Tecnologia / Biblioteca  | Descrição                                              |
|------------------|-------------------------|--------------------------------------------------------|
| **Linguagem**    | Python 3.x              | Linguagem base do projeto                              |
| **GUI**          | `tkinter` + `ttk`       | Interface gráfica, janelas, Treeview e Scrollbar       |
| **Persistência** | `json` (built-in)       | Banco de dados local por usuário em arquivos `.json`   |
| **Clipboard**    | `pyperclip`             | Copia a senha gerada para a área de transferência      |
| **Aleatoriedade**| `random` (built-in)     | Geração de senhas aleatórias                           |
| **Sistema**      | `os` (built-in)         | Criação de diretórios por usuário                      |

---

## 📂 Estrutura do Projeto

```
My Pass/
│
├── main.py               # Código principal com toda a lógica e GUI
├── logo.png              # Logo exibida na janela de senhas
├── cadastro.png          # Imagem da tela de cadastro
├── lp.png                # Mini logo na janela principal
├── lg2.png               # Imagem na janela de gerenciamento
├── blueeye_resized.png   # Ícone do botão ocultar/exibir senhas
│
├── users_data/           # Pasta criada em runtime
│   └── [nome_usuario]/   # Pasta individual por usuário
│       ├── usuarios_bd.json   # Credenciais de login do usuário
│       ├── websites.json      # Senhas cadastradas
│       └── dados.txt          # Backup exportado em .txt
│
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação (Português)
└── README_EN.md          # Documentação (English)
```

> **Arquitetura de isolamento por usuário:** A função `cria_dir_user()` cria automaticamente uma subpasta com o nome do usuário dentro de `users_data/` no primeiro acesso, garantindo total separação dos dados.

---

## 🚀 Como Começar

### Pré-requisitos

- **Python 3.8+** — [Download](https://www.python.org/downloads/)
- **pip** (gerenciador de pacotes)
- Os arquivos de imagem (`.png`) devem estar na **mesma pasta** que `main.py`

### Passo a Passo

**1. Clone o repositório**
```bash
git clone https://github.com/[SEU_USUARIO]/[NOME_DO_REPO].git
cd "Projetos-Pessoais-Iniciais/Tkinter Projects/My Pass"
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Execute o programa**
```bash
python main.py
```

**4. Crie seu cadastro**
- Na tela inicial, clique em **CADASTRAR** e escolha um nome de usuário e senha
- Após o cadastro, faça login para acessar o gerenciador

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
