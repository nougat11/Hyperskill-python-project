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
    guests = dict.fromkeys(names, 0)
    print(guests)
