import random
number = int(input("Enter the number of friends joining (including you): "))
print()
if number <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line: ")
    names = []
    for i in range(number):
        names.append(input())
    print()
    print("Enter the total bill value: ")
    money = int(input())
    money = round(money / number, 2)
    guests = dict.fromkeys(names, money)
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    action = input()
    print()
    if action == "Yes":
        
        print(f"{random.choice(names)} is the lucky one!")
    elif action == "No":
        
        print("No one is going to be lucky")
