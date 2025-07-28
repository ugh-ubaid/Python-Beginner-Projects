# 🏠 Mortgage Calculator (Python)

This is a command-line **Mortgage Calculator** built in Python. It helps users compute their payment amount and total payable amount over the loan term based on various compounding intervals.

## 📌 Features

- Supports different compounding intervals:
  - Monthly
  - Weekly
  - Daily
  - Continuous (uses exponential compounding)
- Takes user input for:
  - Loan amount (Principal)
  - Annual interest rate
  - Loan term (in years)
  - Compounding frequency
- Displays:
  - Payment per period
  - Total number of payments
  - Total amount paid (or future value in continuous compounding)

## 📎 How It Works

The program uses the standard mortgage payment formula for **discrete** compounding:

M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)

Where:
- `P` is the principal amount
- `r` is the interest rate per period
- `n` is the total number of payments
- `M` is the payment per period

For **continuous** compounding, it uses:

A = P * e^(r * t)

Where:
- `e` is Euler's number
- `r` is the annual interest rate
- `t` is the time in years

## 📥 Example


## 🛠 Technologies Used

- Python 3.x
- `math` module (for continuous compounding)

## 📂 How to Run

1. Make sure you have Python installed.
2. Run the script in your terminal:
   ```bash
   python mortgage_calculator.py