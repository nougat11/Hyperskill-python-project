# write your code here
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
      
    guests = dict.fromkeys(names, round(money / number, 2))
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    action = input()
    print()
    if action == "Yes":
        name = random.choice(names)
        print(f"{name} is the lucky one!")
        for key, value in guests.items():
            if key == name:
                guests[key] = 0
            else:
                guests[key] = round(money / (number - 1), 2)
    elif action == "No":
        print("No one is going to be lucky")
    print(guests)
