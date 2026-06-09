<div align="center">

# 🅿️ Gerenciador de Estacionamento

[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)](./LICENSE)

> **Sistema de gerenciamento de vagas de estacionamento via terminal — controle de entradas, saídas e disponibilidade em tempo real.**

🇧🇷 Você está lendo em **Português**. | 🇺🇸 [Read in English](./README_EN.md)

</div>

---

## 📖 Sobre o Projeto

O **Gerenciador de Estacionamento** é uma aplicação de linha de comando desenvolvida em Python para o controle operacional de um estacionamento com **10 vagas**. O operador pode registrar a entrada e saída de veículos, consultar a disponibilidade das vagas em tempo real e liberar vagas individuais ou todas de uma vez.

O projeto possui duas versões neste repositório:

| Versão | Arquivo | Descrição |
|--------|---------|-----------|
| **v1.0** | `estacionamento.py` (esta pasta) | Versão inicial, funcional e simples |
| **v1.5** | `Gerenciador de Estacionamento 1.5/` | Versão aprimorada com banco de dados, tabelas formatadas e relatórios gráficos |

---

## ✨ Funcionalidades Principais

- 🕐 **Cadastro de Horário** — Registra nome do motorista, placa, hora de entrada e hora de saída por vaga
- 🚗 **Liberação de Vaga** — Libera uma vaga específica pelo nome
- 🧹 **Liberação Total** — Esvazia todas as vagas de uma só vez com barra de progresso
- 📊 **Disponibilidade** — Exibe o status atual de cada uma das 10 vagas
- 🚪 **Menu interativo** — Navegação clara e com tratamento de erros

---

## 🛠️ Tecnologias e Ferramentas

| Categoria      | Tecnologia / Biblioteca | Descrição                                        |
|----------------|------------------------|--------------------------------------------------|
| **Linguagem**  | Python 3.x             | Linguagem base do projeto                        |
| **Progresso**  | `tqdm`                 | Barra de progresso ao liberar todas as vagas     |
| **Tempo**      | `time` (built-in)      | Pausas e feedback visual no terminal             |

---

## 📂 Estrutura do Projeto

```
Gerenciador De Estacionamento/
│
├── estacionamento.py                    # v1.0 — versão inicial
├── requirements.txt                     # Dependências da v1.0
├── README.md                            # Documentação (Português)
├── README_EN.md                         # Documentação (English)
│
└── Gerenciador de Estacionamento 1.5/   # v1.5 — versão aprimorada
    ├── estacionamento.py                # Código da v1.5
    ├── requirements.txt                 # Dependências da v1.5
    ├── README.md                        # Documentação da v1.5 (PT-BR)
    └── README_EN.md                     # Documentação da v1.5 (EN)
```

> O estacionamento é modelado como um **dicionário Python** onde cada chave é uma vaga (`'vaga 1'` a `'vaga 10'`) e o valor é uma lista com os dados do veículo. Uma lista vazia significa vaga livre.

---

## 🚀 Como Começar

### Pré-requisitos

- **Python 3.8+** — [Download](https://www.python.org/downloads/)
- **pip** (gerenciador de pacotes)

### Passo a Passo

**1. Clone o repositório**
```bash
git clone https://github.com/[SEU_USUARIO]/[NOME_DO_REPO].git
cd "Projetos-Pessoais-Iniciais/Gerenciador De Estacionamento"
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Execute o programa**
```bash
python estacionamento.py
```

**4. Navegue pelo menu**
```
<< MENU INICIAL >>

[1] - Cadastrar horário
[2] - Liberar vaga
[3] - Liberar todas as vagas
[4] - Disponibilidade das Vagas
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

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/felipe-rodrigues-fonseca-843b9421a/)
[![E-mail](https://img.shields.io/badge/E--mail-Contato-red?style=flat-square&logo=gmail)](mailto:comunidadehawks@gmail.com)
