temperatures = [22, 25, None, 19, 30, None, 27, 18, 35, 100]

# 1. Supprimer les valeurs None
temperatures_clean = []

for temperature in temperatures:
    if temperature is not None:
        temperatures_clean.append(temperature)

print("Températures nettoyées :", temperatures_clean)


# 2. Calculer la moyenne
moyenne = sum(temperatures_clean) / len(temperatures_clean)

print("Moyenne :", moyenne)


# 3. Minimum et maximum
minimum = min(temperatures_clean)
maximum = max(temperatures_clean)

print("Minimum :", minimum)
print("Maximum :", maximum)


# 4. Garder les températures entre 20 et 35
temperatures_normales = []

for temperature in temperatures_clean:
    if 20 <= temperature <= 35:
        temperatures_normales.append(temperature)

print("Températures entre 20 et 35 :", temperatures_normales)


# 5. Compter les températures supérieures à 30
nombre_sup_30 = 0

for temperature in temperatures_clean:
    if temperature > 30:
        nombre_sup_30 += 1

print("Nombre > 30 :", nombre_sup_30)