<div align="center">

# 🍅 Pomodoro Time Manager

[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational?style=for-the-badge&logo=python)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)](./LICENSE)

> **Timer Pomodoro com interface gráfica, alertas sonoros, imagens por ciclo e navegação entre janelas de instruções e informações sobre o autor.**

🇧🇷 Você está lendo em **Português**. | 🇺🇸 [Read in English](./README_EN.md)

</div>

---

## 📖 Sobre o Projeto

O **Pomodoro Time Manager** é uma versão aprimorada de um exercício do curso *100 Days of Code*. A versão original era um timer básico com uma label que indicava o ciclo atual. Esta versão expande a ideia com **alertas sonoros** para cada transição de ciclo, **imagens animadas** trocadas automaticamente a cada fase, uma **janela de instruções** sobre a técnica Pomodoro, e uma **janela "Sobre o Programa"** com links para as redes sociais do autor.

### O que é a Técnica Pomodoro?
Trabalhe por **25 minutos** → pausa de **5 min** → repita 4 vezes → pausa longa de **25 min**.

---

## ✨ Funcionalidades Principais

- ⏱️ **Timer Pomodoro Completo** — Ciclos de trabalho (25 min), pausa curta (5 min) e pausa longa (25 min)
- 🔔 **Alertas Sonoros** — Sons distintos ao iniciar o programa, ao trocar de ciclo e ao finalizar
- 🖼️ **Imagens por Ciclo** — Imagem diferente para cada fase (trabalho, pausa curta, pausa longa)
- ✅ **Contador de Sessões** — Checkmarks (✅) acumulam a cada sessão de trabalho completada
- ▶️ **Botão Start** — Inicia o timer e é desabilitado para evitar duplo clique durante o ciclo
- 🔄 **Botão Reset** — Cancela o ciclo atual e zera o contador com som de reset
- 📋 **Tela de Instruções** — Janela explicando como utilizar o método Pomodoro com o programa
- ℹ️ **Sobre o Programa** — Janela com informações sobre o autor e links para redes sociais

---

## 🛠️ Tecnologias e Ferramentas

| Categoria       | Tecnologia / Biblioteca | Descrição                                              |
|-----------------|------------------------|--------------------------------------------------------|
| **Linguagem**   | Python 3.x             | Linguagem base do projeto                              |
| **GUI**         | `tkinter`              | Interface gráfica com Canvas, Button, Label e Toplevel |
| **Áudio**       | `pygame` (`mixer`)     | Reprodução de sons `.mp3` e `.wav` nos eventos         |
| **Navegador**   | `webbrowser` (built-in)| Abre links externos (redes sociais do autor)           |
| **Matemática**  | `math` (built-in)      | Cálculo de minutos e segundos para o contador          |

---

## 📂 Estrutura do Projeto

```
Pomodoro Time Manager/
│
├── main.py                    # Código principal com toda a lógica e GUI
│
├── clkbanner.png              # Banner do relógio exibido no topo
├── tomato.png                 # Tomate com o timer sobreposto
├── worktime_resized.png       # Imagem da fase de trabalho
├── shortbreak_resized.png     # Imagem da pausa curta
├── longbreak_resized.png      # Imagem da pausa longa
├── cape_resized.png           # Imagem de fundo da tela inicial
├── eu_resized.png             # Foto do autor (tela "Sobre")
├── logopronta_resized.png     # Logo do autor (tela "Sobre")
├── pomoinstruction.png        # Imagem da tela de instruções
├── faceicon.png               # Ícone Facebook
├── kediniconr.png             # Ícone LinkedIn
├── insta2r.jpg                # Ícone Instagram
│
├── apito.mp3                  # Som de alerta de ciclo
├── reset.mp3                  # Som de reset
├── jobdone.mp3                # Som de conclusão
├── start tema.wav             # Tema de abertura da janela do timer
├── instrucoes tema.wav        # Tema da tela de instruções
├── tema abertura.wav          # Tema da tela inicial
│
├── requirements.txt           # Dependências do projeto
├── README.md                  # Documentação (Português)
└── README_EN.md               # Documentação (English)
```

---

## 🚀 Como Começar

### Pré-requisitos

- **Python 3.8+** — [Download](https://www.python.org/downloads/)
- **pip** (gerenciador de pacotes)
- Todos os arquivos de imagem (`.png`, `.jpg`) e áudio (`.mp3`, `.wav`) devem estar na **mesma pasta** que `main.py`

### Passo a Passo

**1. Clone o repositório**
```bash
git clone https://github.com/[SEU_USUARIO]/[NOME_DO_REPO].git
cd "Projetos-Pessoais-Iniciais/Tkinter Projects/Pomodoro Time Manager"
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Execute o programa**
```bash
python main.py
```

**4. Na tela inicial:**
- **START** → Abre o timer Pomodoro
- **INSTRUÇÕES** → Explica como usar o método Pomodoro
- **SOBRE O PROGRAMA** → Informações e contatos do autor

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
