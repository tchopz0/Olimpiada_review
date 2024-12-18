text = "programming"


# --------------------------
# Wycinanie początku i końca
# --------------------------


# Od indeksu 0 do 6 (bez 6)
print(text[0:6])  # "progra"

# Od indeksu 3 do końca
print(text[3:])  # "gramming"

# Od początku do indeksu 5
print(text[:5])  # "progr"

# Cały ciąg
print(text[:])  # "programming"


# --------------------------
# Używanie ujemnych indeksow
# --------------------------


# Ostatnie 3 znaki
print(text[-3:])  # "ing"

# Wszystko bez ostatnich 3 znaków
print(text[:-3])  # "programm"

# Od 2. znaku od końca do ostatniego (bez końcowego)
print(text[-2:-1])  # "n"


# --------------------------
# Używanie kroku step
# --------------------------


# Co drugi znak
print(text[::2])  # "pormig"

# Odwracanie ciągu (krok ujemny)
print(text[::-1])  # "gnimmargorp"

# Wycinanie co trzeci znak od indeksu 1 do końca
print(text[1::3])  # "rmi"


