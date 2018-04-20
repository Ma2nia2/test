print ("Witaj!")

imię = input ("Podaj proszę swoje imie:")
nazwisko = input("Podaj proszę swoje nazwisko:")

print ("Liczba liter z których składa się Twoje nazwisko to:")
print (len(nazwisko))

print ("Liczba liter z ktorych składa się Twoje imię to:")
print (len(imię))

print ("Jako ciekawostkę, pokaż Ci jak wygląda Twoje imię i nazwisko w lustrzanym odbiciu")
print (imię[::-1])
print (nazwisko [::-1])

print ("Podaj mi proszę datę swoich urodzin,a powiem Ci,ktory to dzień roku")

dzień = input ("Podaj dzień")
miesiąc = input ("Podaj miesiąc")


dzień = int(dzień)
miesiąc = int (miesiąc)


x = (dzień + miesiąc * 30 - 30)

print ("Liczba dni jak minęła od poczatku roku do Twoich urodzin to:")

print (x)

print ("Dziękuje i życze miłego dnia")