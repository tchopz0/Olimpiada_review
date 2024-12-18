# Znalezienie najdłuższego wspólnego prefiksu-sufiksu

# -----------------
# Naiwne podejście:
# -----------------

def find_pref_suf(word):
    result = "brak"
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[-i:]
        if prefix == suffix:
            result = prefix
    return result

word = input("Podaj ciąg znaków: ")
print("Najdłuższy prefiks-sufiks:", find_pref_suf(word))


# ----------------------------------
# Tablica prefiksowa (używana w KMP)
# ----------------------------------

def compute_prefix_table(pattern):
    m = len(pattern)
    prefix_table = [0] * m
    j = 0  # Długość bieżącego prefiksu-sufiksu

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_table[i] = j

    return prefix_table

pattern = input("Podaj wzorzec: ")
print("Tablica prefiksowa:", compute_prefix_table(pattern))

