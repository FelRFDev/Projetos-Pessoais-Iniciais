<div align="center">

# 🅿️ Gerenciador de Estacionamento — v1.5

[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)](./LICENSE)

> **Versão aprimorada do gerenciador com banco de dados JSON, cadastro de clientes, cálculo automático de tarifas, tabelas formatadas e relatórios em gráfico de barras com envio por e-mail.**

🇧🇷 Você está lendo em **Português**. | 🇺🇸 [Read in English](./README_EN.md)

</div>

---

## 📖 Sobre o Projeto

A **versão 1.5** do Gerenciador de Estacionamento representa um salto significativo em relação à v1.0. Além de gerenciar as vagas em tempo real, esta versão introduz um sistema completo de cadastro de clientes persistido em JSON, **cálculo automático de tarifas** por tempo de permanência, geração de **relatórios analíticos em gráfico de barras** (Matplotlib) com acumulação mensal de clientes e lucro, e envio do relatório por **e-mail automático**.

> ⚠️ **Este projeto ainda se encontra em desenvolvimento ativo.** Algumas funcionalidades podem apresentar comportamento incompleto.

---

## ✨ Funcionalidades Principais

- 🧑‍💼 **Cadastro de Clientes** — Registra motoristas novos (placa, modelo, CPF) persistidos em `clientes.json`
- 💰 **Cálculo Automático de Tarifas** — Calcula o total a pagar com base nas horas e minutos de permanência
- 📋 **Tabelas Formatadas** — Menus e listagens exibidos com bordas duplas via `PrettyTable`
- 📊 **Relatório por Período** — Gráfico de barras com total de clientes e lucro por mês (Matplotlib)
- 💾 **Dados Mensais Acumulados** — `dadosMensais.json` armazena clientes e lucro mês a mês
- 📧 **Envio de Relatório por E-mail** — O gráfico gerado pode ser enviado automaticamente como anexo
- 🔒 **Modo Admin** — Gera dados simulados para demonstração do relatório gráfico
- 🚗 **Todas as funções da v1.0** — Controle de vagas, disponibilidade, liberação individual e total

---

## 🛠️ Tecnologias e Ferramentas

| Categoria       | Tecnologia / Biblioteca        | Descrição                                          |
|-----------------|-------------------------------|-----------------------------------------------------|
| **Linguagem**   | Python 3.x                    | Linguagem base do projeto                           |
| **Persistência**| `json` (built-in)             | Banco de dados local: clientes e dados mensais      |
| **Tabelas**     | `prettytable`                 | Menus e listas formatados com bordas duplas         |
| **Gráficos**    | `matplotlib`                  | Geração de gráfico de barras por período            |
| **E-mail**      | `smtplib`, `email` (built-in) | Envio automático do relatório `.png` por e-mail     |
| **Progresso**   | `tqdm`                        | Barra de progresso na liberação de vagas            |
| **Data/Hora**   | `datetime` (built-in)         | Timestamp nos e-mails e controle de períodos        |
| **Aleatoriedade**| `random` (built-in)          | Dados simulados no Modo Admin                       |

---

## 📂 Estrutura do Projeto

```
Gerenciador de Estacionamento 1.5/
│
├── estacionamento.py     # Código principal da v1.5
├── clientes.json         # Banco de clientes cadastrados (criado em runtime)
├── dadosMensais.json     # Acumulado mensal de clientes e lucro (criado em runtime)
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação (Português)
└── README_EN.md          # Documentação (English)
```

**Arquitetura de dados:**
- `clientes.json` — Dicionário `{nome: [placa, modelo, cpf]}`
- `dadosMensais.json` — Dicionário com 12 meses, cada um como `[total_clientes, lucro_mensal]`

**Tabela de tarifas (embutida no código):**
```python
precos = { 30: 10,   # R$ 10 a cada 30 minutos
           60: 20 }  # R$ 20 a cada hora
```

---

## 🚀 Como Começar

### Pré-requisitos

- **Python 3.10+** (necessário para `match/case`) — [Download](https://www.python.org/downloads/)
- **pip** (gerenciador de pacotes)

### Passo a Passo

**1. Clone o repositório**
```bash
git clone https://github.com/[SEU_USUARIO]/[NOME_DO_REPO].git
cd "Projetos-Pessoais-Iniciais/Gerenciador De Estacionamento/Gerenciador de Estacionamento 1.5"
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Configure o envio de e-mail** *(opcional)*

Abra `estacionamento.py` e edite a função `EnviaEmail`:
```python
fromaddr = "[SEU_EMAIL@gmail.com]"
server.login(fromaddr, "[SUA_SENHA_DE_APP_GMAIL]")
```
> ⚠️ Use uma **Senha de App** do Gmail: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

**4. Execute o programa**
```bash
python estacionamento.py
```

**5. Menu Principal**
```
MENU INICIAL
╔══════╦══════════════════════════════════╗
║ CÓDIGO ║ OPÇÕES                         ║
╠══════╬══════════════════════════════════╣
║ 1    ║ Cadastrar horário               ║
║ 2    ║ Liberar vaga                    ║
║ 3    ║ Liberar todas as vagas          ║
║ 4    ║ Disponibilidade das Vagas       ║
║ 5    ║ Finalizar Diária                ║
║ 6    ║ Gerar Relatório                 ║
║ 7    ║ Sair                            ║
║ 8    ║ Gerar Relatório (VERSÃO ADMIN)  ║
╚══════╩══════════════════════════════════╝
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

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/felipe-rodrigues-fonseca-843b9421a/)
[![E-mail](https://img.shields.io/badge/E--mail-Contato-red?style=flat-square&logo=gmail)](mailto:comunidadehawks@gmail.com)
