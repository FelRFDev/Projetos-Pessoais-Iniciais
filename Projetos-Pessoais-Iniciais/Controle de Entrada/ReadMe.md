<div align="center">

# 📋 Controle de Entrada

[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)](./LICENSE)

> **Sistema de portaria via terminal para registro e controle de entradas e saídas de visitantes, com envio automatizado de relatórios por e-mail.**

🇧🇷 Você está lendo em **Português**. | 🇺🇸 [Read in English](./README_EN.md)

</div>

---

## 📖 Sobre o Projeto

O **Controle de Entrada** é uma aplicação de linha de comando desenvolvida em Python para ser utilizada em portarias e recepções. Ele resolve o problema de registrar manualmente entradas e saídas de visitantes, motoristas e caminhões, centralizando todos os dados em um banco de dados local (`.json`) e permitindo o envio automatizado de um relatório diário por e-mail ao final do expediente.

O projeto possui duas versões:
- **`ControleDeEntradaTXT.py`** — Gera relatórios em formato `.txt`
- **`ControledeEntradaWord.py`** — Gera relatórios formatados em tabela no formato `.docx` (Microsoft Word)

---

## ✨ Funcionalidades Principais

- 📝 **Registro de Entrada** — Cadastra nome, placa do veículo e horário de entrada do visitante
- 🚪 **Registro de Saída** — Registra o horário de saída por nome do visitante
- 🔍 **Consulta de Registros** — Exibe todos os registros do dia formatados no terminal
- ✏️ **Edição de Dados** — Permite corrigir o nome de um visitante já cadastrado
- 🗑️ **Limpeza de Cadastro** — Apaga todos os registros com confirmação de segurança
- 📧 **Envio por E-mail** — Gera o relatório e o envia como anexo por e-mail via SMTP (Gmail)
- 📄 **Exportação para Word** — *(Versão Word)* Exporta os dados para uma tabela formatada em `.docx`

---

## 🛠️ Tecnologias e Ferramentas

| Categoria       | Tecnologia / Biblioteca        | Descrição                                    |
|-----------------|-------------------------------|----------------------------------------------|
| **Linguagem**   | Python 3.x                    | Linguagem base do projeto                    |
| **Persistência**| `json` (built-in)             | Banco de dados local em arquivo `.json`      |
| **E-mail**      | `smtplib`, `email` (built-in) | Envio de e-mail com anexo via SMTP (Gmail)   |
| **Progresso**   | `tqdm`                        | Barra de progresso visual no terminal        |
| **Tempo**       | `datetime`, `time` (built-in) | Controle de datas e pausas                   |
| **Word**        | `python-docx`                 | Geração de relatório em `.docx` *(v. Word)*  |

---

## 📂 Estrutura do Projeto

```
Controle de Entrada/
│
├── ControleDeEntradaTXT.py    # Versão com relatório em .txt e envio por e-mail
├── ControledeEntradaWord.py   # Versão com relatório em tabela .docx
├── bd.json                    # Banco de dados local (criado em tempo de execução)
├── registro.txt               # Arquivo de registro auxiliar (criado em tempo de execução)
├── requirements.txt           # Dependências do projeto
├── README.md                  # Documentação (Português)
└── README_EN.md               # Documentação (English)
```

> O arquivo `bd.json` centraliza todos os registros de visitantes. As classes `BancoDados` e `bdFuncoes` encapsulam, respectivamente, a criação e a manipulação desses dados.

---

## 🚀 Como Começar

### Pré-requisitos

Certifique-se de ter instalado em sua máquina:

- **Python 3.8+** — [Download](https://www.python.org/downloads/)
- **pip** (gerenciador de pacotes, já incluso com o Python)

### Passo a Passo

**1. Clone o repositório**
```bash
git clone https://github.com/[SEU_USUARIO]/[NOME_DO_REPO].git
cd "Projetos-Pessoais-Iniciais/Controle de Entrada"
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Configure o envio de e-mail**

Antes de executar, abra o arquivo `.py` desejado e preencha as variáveis de e-mail:
```python
fromaddr = "[SEU_EMAIL@gmail.com]"      # E-mail remetente
toaddr   = "[EMAIL_DESTINATARIO@...]"   # E-mail destinatário
# ...
server.login(fromaddr, "[SUA_SENHA_DE_APP_GMAIL]")
```
> ⚠️ Recomenda-se usar uma **Senha de App** do Gmail, não a sua senha principal. Crie uma em: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

**4. Execute o programa**

Para a versão com relatório em `.txt`:
```bash
python ControleDeEntradaTXT.py
```

Para a versão com relatório em `.docx`:
```bash
python ControledeEntradaWord.py
```

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

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue?style=flat-square&logo=linkedin)]([SEU_LINKEDIN])
[![E-mail](https://img.shields.io/badge/E--mail-Contato-red?style=flat-square&logo=gmail)](mailto:[SEU_EMAIL])
