print("donne moi un liste des nombre ")
nombre = input().split()
for i in range(len(nombre)):
    if int(nombre[i]) % 2 == 0:
        print(nombre[i], "est un nombre pair ")
    else:
        print(nombre[i], "est un nombre impair ")
        