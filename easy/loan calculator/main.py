import math
print('Enter the loan principal:')
loan_principal = int(input())
print("""
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment
""")
action = input()
if action == 'm':
    print("Enter the monthly payment:")
    payment = int(input())
    months = math.ceil(loan_principal / payment)
    if months != 1:
        print(f"It will take {months} months to repay the loan")
    else:
        print(f"It will take {months} month to repay the loan")
else:
    print("Enter the number of months:")
    months = int(input())
    payment = math.ceil(loan_principal / months)
    if months % payment == 0:
        print(f"Your monthly payment = {payment}")
    else:
        print(f"Your monthly payment = {payment} and the last payment = {loan_principal - payment * (months - 1)}.")
