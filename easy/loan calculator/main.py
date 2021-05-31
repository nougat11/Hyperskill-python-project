import math

print("""
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
""")
action = input()
if action == 'n':
    print('Enter the loan principal:')
    loan_principal = int(input())
    print("Enter the monthly payment:")
    payment = int(input())
    print("Enter the loan interest:")
    loan_interest = float(input())
    i = loan_interest / 1200
    n = math.log(payment/(payment - i * loan_principal), 1 + i)
    n = math.ceil(n)
    print(n)
    years = n // 12
    months = n % 12
    mask_ans = ""
    if years == 1:
        mask_ans = mask_ans + "1 year"
    elif years > 0:
        mask_ans = mask_ans + f'{years} years '
    if years > 0 and months > 0:
        mask_ans = mask_ans + 'and '
    if months == 1:
        mask_ans = mask_ans + "1 month"
    elif months > 0:
        mask_ans = mask_ans + f'{months} months '
    print(f'It will take {mask_ans}to repay this loan!')
elif action == 'a':
    print('Enter the loan principal:')
    loan_principal = int(input())
    print("Enter the number of periods")
    months = int(input())
    print("Enter the loan interest:")
    loan_interest = float(input())
    i = loan_interest / 1200
    a = loan_principal * ((i * (i + 1) ** months) / ((1 + i) ** months - 1))
    print(f'Your monthly payment = {math.ceil(a)}!')
elif action == 'p':
    print('Enter the annuity payment::')
    annuity_principal = float(input())
    print("Enter the number of periods")
    months = int(input())
    print("Enter the loan interest:")
    loan_interest = float(input())
    i = loan_interest / 1200
    ans = annuity_principal / (((i * (1 + i) ** months)) / ((1 + i) ** months - 1))
    print(f'Your loan principal = {math.ceil(ans)}!')
