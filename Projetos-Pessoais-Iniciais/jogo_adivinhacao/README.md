<div align="center">

# 🎯 Jogo de Adivinhação

[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)](./LICENSE)

> **Jogo interativo de terminal onde o jogador tem 3 vidas para adivinhar o número sorteado pelo computador — com arte ASCII dinâmica e feedback visual.**

🇧🇷 Você está lendo em **Português**. | 🇺🇸 [Read in English](./README_EN.md)

</div>

---

## 📖 Sobre o Projeto

O **Jogo de Adivinhação** é um game simples de terminal desenvolvido em Python para praticar lógica de programação, estruturas condicionais e manipulação de dicionários. A cada rodada, o computador sorteia um número entre 1 e 10, e o jogador tem **3 vidas** para acertá-lo.

A grande sacada do projeto é o sistema de feedback visual: a cada vida perdida, uma arte ASCII de corações diminui em tempo real no terminal, criando uma experiência imersiva mesmo sem interface gráfica.

---

## ✨ Funcionalidades Principais

- 🎲 **Sorteio Aleatório** — Número sorteado com `random.randint` a cada nova partida
- ❤️ **Sistema de Vidas** — O jogador começa com 3 vidas, exibidas como arte ASCII animada
- 🖥️ **Feedback Visual no Terminal** — Arte ASCII de corações diminui conforme as vidas são perdidas
- 🏆 **Condição de Vitória** — Exibe troféu em arte ASCII ao acertar o número
- 💀 **Game Over** — Mensagem clara ao esgotar todas as tentativas
- 🧑 **Personalização** — O jogo solicita o nome do jogador e o usa durante toda a partida

---

## 🛠️ Tecnologias e Ferramentas

| Categoria      | Tecnologia / Biblioteca | Descrição                                         |
|----------------|------------------------|---------------------------------------------------|
| **Linguagem**  | Python 3.x             | Linguagem base do projeto                         |
| **Aleatoriedade** | `random` (built-in) | Sorteio do número a ser adivinhado                |

> ✅ Nenhuma dependência externa. O projeto roda com a instalação padrão do Python.

---

## 📂 Estrutura do Projeto

```
jogo_adivinhacao/
│
├── main.py         # Código principal com toda a lógica do jogo
├── README.md       # Documentação (Português)
└── README_EN.md    # Documentação (English)
```

**Fluxo do programa:**
- `player_lifes_stages` — Dicionário que mapeia o número de vidas restantes (3, 2, 1) à sua representação em arte ASCII
- `numero_sorteado` — Número aleatório gerado uma vez por partida
- Loop principal — Recebe o palpite do jogador, compara com o sorteado e decide o estado do jogo

---

## 🚀 Como Começar

### Pré-requisitos

- **Python 3.8+** — [Download](https://www.python.org/downloads/)

### Passo a Passo

**1. Clone o repositório**
```bash
git clone https://github.com/[SEU_USUARIO]/[NOME_DO_REPO].git
cd "Projetos-Pessoais-Iniciais/jogo_adivinhacao"
```

**2. Instale as dependências**

Este projeto usa apenas a biblioteca nativa `random`. Nenhuma instalação adicional é necessária.

**3. Execute o jogo**
```bash
python main.py
```

**4. Jogue!**
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

## 🤝 Como Contribuir

1. Faça um **Fork** do projeto
2. Crie uma branch para sua feature: `git checkout -b feature/minha-feature`
3. Faça suas alterações e commit: `git commit -m 'feat: adiciona minha feature'`
4. Envie para a branch: `git push origin feature/minha-feature`
5. Abra um **Pull Request**

**Sugestões de melhorias:**
- 🎯 Adicionar dicas de "quente/frio" (maior ou menor)
- 🏅 Sistema de pontuação e ranking
- 🔄 Opção de jogar novamente sem reiniciar o script
- 🎨 Adicionar cores com `colorama`

---

## 📝 Licença e Contato

Este projeto está licenciado sob a **Licença MIT**. Consulte o arquivo `LICENSE` para mais detalhes.

**Autor:** Felipe Rodrigues Fonseca

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue?style=flat-square&logo=linkedin)]([SEU_LINKEDIN])
[![E-mail](https://img.shields.io/badge/E--mail-Contato-red?style=flat-square&logo=gmail)](mailto:[SEU_EMAIL])
