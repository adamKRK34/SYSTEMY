def sumuj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b != 0:
        return a / b
    else:
        return "Błąd! Nie można dzielić przez zero."

print("Witaj w super kalkulatorze!")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")

wybor = input("Wybierz numer operacji (1/2/3/4): ")

if wybor in ('1', '2', '3', '4'):
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    if wybor == '1':
        print(liczba1, "+", liczba2, "=", sumuj(liczba1, liczba2))
    elif wybor == '2':
        print(liczba1, "-", liczba2, "=", odejmij(liczba1, liczba2))
    elif wybor == '3':
        print(liczba1, "*", liczba2, "=", pomnoz(liczba1, liczba2))
    elif wybor == '4':
        print(liczba1, "/", liczba2, "=", podziel(liczba1, liczba2))
else:
    print("Błąd! Wybierz poprawny numer operacji.")
