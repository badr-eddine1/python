print("donne moi un mot de passe ")
mdp = input()
if len(mdp) < 8:
    print("longueur non ")
else:
    print("longueur ok ")

for i in mdp:
    if mdp[i].isupper():
        print("majuscules ok ")
        break
    elif mdp[i].islower():
        print("minuscules ok ")
        break
    elif mdp[i].isdigit():
        print("chiffres ok ")
        break
    