# Loan Amortization Calculator (Python)
#
# Overview
# This project generates a full loan amortization schedule and exports the results
# to a CSV file. It takes common loan parameters as input and produces a month-by-month
# breakdown of remaining balance and total interest accrued, compatible with Excel.
#
# This project was built to practice reading/writing CSV-style output using Python and to
# mirror real workflows I encounter in real estate, operations, and analytics.
#
# Features
# - Calculates fixed monthly payments using the standard amortization formula
# - Simulates repayment month-by-month until the balance reaches near-zero
# - Tracks cumulative interest accrued over time
# - Exports results to a spreadsheet-friendly CSV file
#
# Inputs (User Prompts)
# - Output CSV filename
# - Principal amount (P)
# - Term length in months (N)
# - Annual interest rate as a decimal (i)  (example: 0.025 for 2.5%)
#
# Output (CSV File)
# - Header row: Month,Total Accrued Interest,Loan Balance
# - Includes a Month 0 baseline row (starting balance, $0 interest)
# - One row per month until the loan balance is effectively $0.00
#
# How It Works (High-Level)
# 1) Read inputs from user
# 2) Convert annual interest rate to a monthly rate (i / 12)
# 3) Compute the fixed monthly payment using the amortization formula
# 4) Initialize tracking variables (month count, balance, total interest)
# 5) Write CSV header and month 0 state
# 6) Loop monthly:
#    - Compute monthly interest = balance * monthly_rate
#    - Update total interest accrued
#    - Update balance = balance + monthly_interest - monthly_payment
#    - Clamp balance to 0 if rounding pushes it negative
#    - Write month results to CSV
#
# Potential Use Cases
# - Mortgage / loan analysis for real estate decisions
# - Financial modeling and reporting workflows using CSV exports
# - Operational decision-support and scenario comparisons
#
# Future Improvements
# - Add input validation (non-numeric, negative values, zero-interest handling)
# - Refactor into functions for reusability and testing
# - Output additional columns (monthly interest, principal paid, payment amount)
# - Add charting/visualization support
#
# Author
# Marc Duncan
# Industrial Engineering Student (Texas A&M)
