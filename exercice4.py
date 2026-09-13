notes = [12, 15, 8, 17, 10, 14, 6, 19, 11, 16]

# 1. Afficher les notes
print("Notes :", notes)

# 2. Calculer la moyenne
moyenne = sum(notes) / len(notes)
print("Moyenne :", moyenne)

# 3. Note maximale
note_max = max(notes)
print("Note maximale :", note_max)

# 4. Note minimale
note_min = min(notes)
print("Note minimale :", note_min)

# 5. Compter les étudiants admis
nombre_admis = 0

for note in notes:
    if note >= 10:
        nombre_admis += 1

print("Nombre d'admis :", nombre_admis)

# 6. Afficher les notes des étudiants ayant échoué
print("Notes des étudiants ayant échoué :")

for note in notes:
    if note < 10:
        print(note)

# 7. Résultat général
if moyenne >= 10:
    print("Résultat : Admis")
else:
    print("Résultat : Échec")