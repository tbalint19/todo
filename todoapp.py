import os.path

x = input("Please specify a command[list, add, mark, archive]: ")

if x == "add" :
    a = input("Add an item: ")

    y=open("lista.txt","a")
    y.write(a + "\n")
    y.close
    print("Item added")

if x == "list" :

    if os.path.isfile("lista.txt") is True :

        y=open("lista.txt","r")
        lista = y.readlines()
        k=0
        for u in lista:
            k=+1
            print(k, "[]" + u)

        y.close()

    else :
        y = open("lista.txt", "w")


if x == "archive" :

    if os.path.isfile("lista.txt") is True :

        y=open("lista.txt","r")
        lista = y.readlines()
        k=0
        for u in lista:

            print("[]" + k + u)
            k=+1

        y.close()

        z = (int(input("Choose an item to remove: ")))

        remove

    else :

        y = open("lista.txt", "w")
