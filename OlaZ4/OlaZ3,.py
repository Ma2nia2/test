lista  = input("Wprowadz ciąg znaków,składjący sie z cyfr i liter")

liczby = 0
cyfry = 0


for znak in lista:
    if znak in "1234567890":
        liczby = liczby + 1
    else:
        cyfry = cyfry + 1
print("Liter w ciąg jest", liczby)


print("Cyfr w ciągu jest",cyfry)


