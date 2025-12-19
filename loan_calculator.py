# Name:        Marc Duncan
# Section:     559
# Project:     loan calculator (individual)
# Date:        11/02/2025

#inputs for collecting filename, principal amount, term length, annual interest rate.
file_name = input("Enter the output filename: ")
principal_amt = float(input("Enter the principal amount: "))
term_len = int(input("Enter the term length (months): "))
annual_int = float(input("Enter the annual interest rate: "))

#rate and monthly payment calculations
rate = annual_int / 12
monthly_payment = (principal_amt * rate) / (1 - (1 + rate) ** (-term_len))

#loop variables for initalizing
month_ct = 0
balance = principal_amt
total_interest = 0.0

#opening the file to write the calculations on
with open(file_name, "w") as j:
    j.write('Month,Total Accrued Interest,Loan Balance\n')
    j.write(f'0,$0.00,${balance:.2f}\n')

#while loop when the balance is greater than 0.01
    while balance > 0.01:
        month_ct += 1
        monthly_interest = balance * rate
        total_interest = total_interest + monthly_interest
        balance = balance + monthly_interest - monthly_payment

#condition to check if the balance has reached zero
        if balance < 0:
            balance = 0.00

#write the information on the new file 
        j.write(f'{month_ct},${total_interest:.2f},${balance:.2f}\n')

