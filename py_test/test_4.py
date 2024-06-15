
dicti = {'1': 'Book1', '2': 'Book2', '3': 'Book3'}


def display():
    print(" *** Books available in Inventory*** ")
    for key in dicti:
        print("\t" + str(key) + "\t" + dicti[key])


def choice():
    try:
        ch = int(input())
        return ch
    except:
        print('***please enter number only ***')
        return choice()


def add():
    print("Enter Book Name")
    dicti[len(dicti) + 1] = input()
    print(dicti[len(dicti)] + " Book entered successfully")


def remove():
    if not bool(dicti):
        print("Books are not available to remove")
    else:
        display()
        print("enter index of book you want to remove")
        index = input()
        if not index in dicti:
            print("entered wrong index")
        else:
            dicti.pop(index)


print("\n 1. Add a Book\n 2. Remove a Book\n 3. List of Books\n 4. Enter 0 to Exit")
print("Please enter your Choice:")
ch = choice()

while ch != 0:
    if ch == 1:
        add()
    elif ch == 2:
        remove()
    elif ch == 3:
        display()
    else:
        print("Enter correct option:")
    print("\n 1. Add a Book\n 2. Remove a Book\n 3. List of Books\n 4. Enter 0 for Exit")
    print("Please enter your Choice:")
    ch = choice()