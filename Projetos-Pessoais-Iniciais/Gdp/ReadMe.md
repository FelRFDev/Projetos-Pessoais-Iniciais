<div align="center">

# 🏢 G.D.P — Gestão de Portaria

[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)](./LICENSE)

> **Sistema completo de gestão de portaria via terminal — controle de chaves, ramais, projetores e lista de afazeres com assistente virtual por voz integrada.**

🇧🇷 Você está lendo em **Português**. | 🇺🇸 [Read in English](./README_EN.md)

</div>

---

## 📖 Sobre o Projeto

O **G.D.P (Gestão de Portaria)** é o projeto mais completo deste repositório. Desenvolvido para uso real em ambiente de trabalho, centraliza em uma única ferramenta de terminal todas as tarefas rotineiras de uma portaria: controle de chaves físicas com numeração, lista de ramais telefônicos, agenda de afazeres, gerenciamento de projetores e cobrança de materiais.

Além do menu manual, o sistema conta com a **Vírtua** — uma assistente virtual ativada por voz que reconhece comandos em português, abre o navegador, pesquisa músicas no YouTube, consulta ramais e chaves por voz, busca informações na Wikipedia e muito mais.

O projeto possui duas versões:

| Versão | Pasta | Diferencial |
|--------|-------|-------------|
| **v1.0** | `Gdp/` (esta pasta) | Versão original estável |
| **v1.5.1** | `Gdp/Gdp 1.5.1/` | Layout aprimorado com arte ASCII nos banners e menus |

---

## ✨ Funcionalidades Principais

- 🗝️ **Controle de Chaves** — Cadastra, remove, edita e consulta chaves físicas com nome e número associado
- 📞 **Controle de Ramais** — Gerencia o catálogo de ramais telefônicos do local
- ✅ **Lista de Afazeres** — Agenda de tarefas do dia para o operador de portaria
- 📋 **Alterações no Setor** — Registra mudanças e eventos relevantes do dia em JSON
- 📽️ **Controle de Projetores** — Gerencia a disponibilidade dos equipamentos de projeção
- 💰 **Cobrança de Materiais** — Registra e acompanha materiais cobrados
- 🤖 **Assistente Virtual "Vírtua"** — Reconhece comandos de voz em PT-BR e executa ações:
  - 🌐 Abrir navegador e pesquisar no Google
  - 🎵 Reproduzir músicas no YouTube (`pywhatkit`)
  - 📅 Informar o dia da semana e as horas atuais
  - 📖 Consultar a Wikipedia e ler o resultado em voz alta
  - 😄 Contar piadas
  - 🗝️ Consultar ramais e chaves por comando de voz

---

## 🛠️ Tecnologias e Ferramentas

| Categoria          | Tecnologia / Biblioteca    | Descrição                                           |
|--------------------|---------------------------|-----------------------------------------------------|
| **Linguagem**      | Python 3.10+              | Necessário para `match/case`                        |
| **Persistência**   | `txt` + `json` (built-in) | Banco de dados via arquivos `.txt` e `.json`        |
| **Relatório**      | `python-docx`             | Geração de documentos Word                          |
| **Progresso**      | `tqdm`                    | Barra de progresso visual                           |
| **TTS (Fala)**     | `pyttsx3`                 | Conversão de texto em fala (offline)                |
| **STT (Escuta)**   | `SpeechRecognition`       | Reconhecimento de voz via Google API                |
| **Navegador**      | `webbrowser` (built-in)   | Abertura de URLs no navegador padrão                |
| **YouTube**        | `pywhatkit`               | Pesquisa e reprodução de músicas no YouTube         |
| **Wikipedia**      | `wikipedia`               | Busca e leitura de artigos da Wikipedia             |
| **Data/Hora**      | `datetime`, `time`        | Informação de dia/hora para a assistente            |

---

## 📂 Estrutura do Projeto

```
Gdp/
│
├── Gdp.py              # Programa principal — menus e lógica de portaria
├── funcoes.py          # Módulo com funções utilitárias e lógica da assistente Vírtua
│
├── chaves.txt          # Banco de chaves (criado em runtime)
├── nums.txt            # Banco de números das chaves (criado em runtime)
├── NomeRamal.txt       # Banco de ramais — nomes (criado em runtime)
├── NumRamal.txt        # Banco de ramais — números (criado em runtime)
├── Afazeres.txt        # Lista de afazeres (criado em runtime)
├── Alt.json            # Alterações no setor (criado em runtime)
├── Projetores.json     # Estado dos projetores (criado em runtime)
│
├── requirements.txt    # Dependências do projeto
├── README.md           # Documentação (Português)
├── README_EN.md        # Documentação (English)
│
└── Gdp 1.5.1/          # Versão 1.5.1 — layout aprimorado
    ├── Gdp.py
    ├── funcoes.py
    ├── requirements.txt
    ├── README.md
    └── README_EN.md
```

**Arquitetura modular:**
> `Gdp.py` importa todas as funções de `funcoes.py` (dentro de uma pasta configurável). A pasta deve ser ajustada no `import` no topo do `Gdp.py`:
> ```python
> from mundo2.funcoes import *   # ← altere "mundo2" para o nome da sua pasta
> ```

---

## 🚀 Como Começar

### Pré-requisitos

- **Python 3.10+** — [Download](https://www.python.org/downloads/)
- **Microfone** — Necessário para usar a Assistente Virtual Vírtua
- **pip** (gerenciador de pacotes)

### Passo a Passo

**1. Clone o repositório**
```bash
git clone https://github.com/[SEU_USUARIO]/[NOME_DO_REPO].git
cd "Projetos-Pessoais-Iniciais/Gdp"
```

**2. Coloque `funcoes.py` dentro de uma pasta**

Crie uma pasta (ex.: `mundo2`) e mova `funcoes.py` para dentro:
```
Gdp/
└── mundo2/
    └── funcoes.py
```

**3. Ajuste o import em `Gdp.py`**

```python
# Linha 1 de Gdp.py — troque o nome da pasta conforme o nome que você escolheu
from mundo2.funcoes import *
```

**4. Instale as dependências**
```bash
pip install -r requirements.txt
```

**5. Execute o programa**
```bash
python Gdp.py
```

**6. Menu principal**
```
----=<<<<<<<<<<<MENU PRINCIPAL>>>>>>>>>>>>=--
1 - ACESSAR MENU
2 - UTILIZAR ASSISTENTE VIRTUAL (VÍRTUA)
3 - SAIR
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
