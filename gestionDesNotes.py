notes =  [8, 12, 15, 17, 20]
print("notes = ", notes[:])
moyenne = sum(notes) / len(notes)
print("moyenne est ", moyenne)
for note in notes:
    if note < moyenne :
        print("echec ")
    if note >= moyenne :
        if note < 12:
            print("passable ")
        elif note >= 12 and note < 16:
            print("bien ")
        elif note >= 16 :
            print("tres bien ")