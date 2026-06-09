<div align="center">

# 🔐 Sistema de Login

[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)](./LICENSE)

> **Sistema de autenticação via terminal com cadastro, login, recuperação e alteração de senha — persistência em JSON e notificação por e-mail.**

🇧🇷 Você está lendo em **Português**. | 🇺🇸 [Read in English](./README_EN.md)

</div>

---

## 📖 Sobre o Projeto

O **Sistema de Login** é uma aplicação de linha de comando que implementa um fluxo completo de autenticação de usuários sem depender de nenhum framework ou banco de dados externo. Os dados são armazenados em um arquivo `.json` local, tornando o projeto totalmente portátil.

Foi desenvolvido como um módulo reutilizável: o bloco marcado como `#BLOCO PARA INSERIR O PROGRAMA DESEJADO` permite que qualquer outra aplicação seja "ancorada" após um login bem-sucedido, transformando este sistema em uma camada de autenticação plug-and-play.

---

## ✨ Funcionalidades Principais

- 👤 **Cadastro** — Registra nome completo, e-mail (usado como usuário) e senha
- 🔑 **Login com Tentativas Limitadas** — Bloqueia após 5 tentativas incorretas de usuário ou senha
- 📧 **Recuperação de Acesso** — Envia os dados de login para o e-mail cadastrado via SMTP
- 🔒 **Alteração de Senha** — Permite redefinir a senha com validação da senha anterior
- 💾 **Persistência Local** — Todos os dados são salvos em `usuarios.json`, sem necessidade de banco de dados externo

---

## 🛠️ Tecnologias e Ferramentas

| Categoria       | Tecnologia / Biblioteca        | Descrição                                       |
|-----------------|-------------------------------|--------------------------------------------------|
| **Linguagem**   | Python 3.x                    | Linguagem base do projeto                       |
| **Persistência**| `json` (built-in)             | Armazenamento local dos usuários em `.json`     |
| **E-mail**      | `smtplib`, `email` (built-in) | Envio de e-mail de recuperação via SMTP (Gmail) |
| **Data**        | `datetime` (built-in)         | Data de envio no corpo do e-mail                |
| **Tempo**       | `time` (built-in)             | Pausas e feedback visual no terminal            |

---

## 📂 Estrutura do Projeto

```
Sistema de Login/
│
├── LoginSystem.py      # Código principal com toda a lógica de autenticação
├── usuarios.json       # Banco de dados local (criado em tempo de execução)
├── requirements.txt    # Dependências do projeto (somente bibliotecas nativas)
├── README.md           # Documentação (Português)
└── README_EN.md        # Documentação (English)
```

> A função `CriaBD()` é chamada no início da execução e garante que o `usuarios.json` seja criado caso não exista. Cada usuário é armazenado como uma lista `[nome, email, senha]` dentro de uma lista principal.

---

## 🚀 Como Começar

### Pré-requisitos

- **Python 3.8+** — [Download](https://www.python.org/downloads/)

### Passo a Passo

**1. Clone o repositório**
```bash
git clone https://github.com/[SEU_USUARIO]/[NOME_DO_REPO].git
cd "Projetos-Pessoais-Iniciais/Sistema de Login"
```

**2. Instale as dependências**

Este projeto usa apenas bibliotecas nativas do Python. Nenhuma instalação adicional é necessária.

**3. Configure o envio de e-mail de recuperação**

Abra `LoginSystem.py` e preencha as variáveis da função `EnviaEmail`:
```python
fromaddr = "[SEU_EMAIL@gmail.com]"   # E-mail remetente (conta que envia a recuperação)
# A senha de login também precisa ser configurada:
server.login(fromaddr, "[SUA_SENHA_DE_APP_GMAIL]")
```
> ⚠️ Use uma **Senha de App** do Gmail. Crie uma em: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

**4. Execute o programa**
```bash
python LoginSystem.py
```

**5. Navegue pelo menu**
```
>>>>>>>  ÁREA DE ACESSO <<<<<<<<

[1] - Cadastrar
[2] - Fazer login
[3] - Recuperar Acesso
[4] - Alterar Senha
[5] - Sair
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
