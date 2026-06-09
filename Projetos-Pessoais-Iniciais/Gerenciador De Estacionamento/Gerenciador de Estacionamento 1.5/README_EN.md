<div align="center">

# 🅿️ Parking Lot Manager — v1.5

[![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

> **Enhanced version of the parking manager featuring a JSON database, customer registration, automatic fare calculation, formatted tables, bar chart reports, and automated email delivery.**

🇺🇸 You are reading in **English**. | 🇧🇷 [Leia em Português](./README.md)

</div>

---

## 📖 About the Project

**Version 1.5** of the Parking Lot Manager is a significant upgrade over v1.0. In addition to real-time spot management, this version introduces a full customer registration system persisted in JSON, **automatic fare calculation** based on parking duration, generation of **analytical bar chart reports** (Matplotlib) with monthly customer count and revenue accumulation, and the ability to **email reports automatically**.

> ⚠️ **This project is still under active development.** Some features may exhibit incomplete behavior.

---

## ✨ Main Features

- 🧑‍💼 **Customer Registration** — Records new drivers (plate, model, CPF) persisted in `clientes.json`
- 💰 **Automatic Fare Calculation** — Computes total due based on hours and minutes of stay
- 📋 **Formatted Tables** — Menus and listings rendered with double borders via `PrettyTable`
- 📊 **Period Report** — Bar chart with total customers and revenue per month (Matplotlib)
- 💾 **Accumulated Monthly Data** — `dadosMensais.json` stores customers and revenue month by month
- 📧 **Email Report Delivery** — Generated chart can be automatically emailed as an attachment
- 🔒 **Admin Mode** — Generates simulated data to demonstrate the graphical report
- 🚗 **All v1.0 Features** — Spot control, availability, individual and full release

---

## 🛠️ Technologies & Tools

| Category        | Technology / Library          | Description                                        |
|-----------------|-------------------------------|-----------------------------------------------------|
| **Language**    | Python 3.x                    | Project's base language                             |
| **Persistence** | `json` (built-in)             | Local database: customers and monthly data          |
| **Tables**      | `prettytable`                 | Double-bordered formatted menus and lists           |
| **Charts**      | `matplotlib`                  | Bar chart generation by period                      |
| **Email**       | `smtplib`, `email` (built-in) | Automatic `.png` report delivery via email          |
| **Progress**    | `tqdm`                        | Progress bar when releasing spots                   |
| **Date/Time**   | `datetime` (built-in)         | Email timestamps and period control                 |
| **Randomness**  | `random` (built-in)           | Simulated data in Admin Mode                        |

---

## 📂 Architecture & Project Structure

```
Gerenciador de Estacionamento 1.5/
│
├── estacionamento.py     # v1.5 main source code
├── clientes.json         # Registered customers database (created at runtime)
├── dadosMensais.json     # Monthly customer/revenue accumulator (created at runtime)
├── requirements.txt      # Project dependencies
├── README.md             # Documentation (Português)
└── README_EN.md          # Documentation (English)
```

**Data architecture:**
- `clientes.json` — Dictionary `{name: [plate, model, cpf]}`
- `dadosMensais.json` — Dictionary with 12 months, each as `[total_customers, monthly_revenue]`

**Pricing table (embedded in code):**
```python
precos = { 30: 10,   # R$ 10 per 30 minutes
           60: 20 }  # R$ 20 per hour
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** (required for `match/case`) — [Download](https://www.python.org/downloads/)
- **pip** (package manager)

### Step-by-Step

**1. Clone the repository**
```bash
git clone https://github.com/[YOUR_USERNAME]/[REPO_NAME].git
cd "Projetos-Pessoais-Iniciais/Gerenciador De Estacionamento/Gerenciador de Estacionamento 1.5"
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure email delivery** *(optional)*

Open `estacionamento.py` and edit the `EnviaEmail` function:
```python
fromaddr = "[YOUR_EMAIL@gmail.com]"
server.login(fromaddr, "[YOUR_GMAIL_APP_PASSWORD]")
```
> ⚠️ Use a **Gmail App Password**: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

**4. Run the program**
```bash
python estacionamento.py
```

---

## 🤝 How to Contribute

1. **Fork** the project
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'feat: add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a **Pull Request**

---

## 📝 License & Contact

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

**Author:** Felipe Rodrigues Fonseca

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/felipe-rodrigues-fonseca-843b9421a/)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat-square&logo=gmail)](mailto:comunidadehawks@gmail.com)
