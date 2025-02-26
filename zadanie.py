from datetime import datetime

dane = input("Podaj swoje imię i nazwisko: ")
imie, nazwisko = dane.split()
nazwisko = nazwisko.upper()
rok_urodzenia = int(input("Podaj swój rok urodzenia: "))
wiek = datetime.now().year-rok_urodzenia

if imie[-1] == "a":
    plec = "kobietą"
else:
    plec = "mężczyzną"

print(
f"""Cześć {imie} {nazwisko}! Twój rok urodzenia to {rok_urodzenia}!
Twoje imie ma {len(imie)} liter, a nazwisko {len(nazwisko)}.
Masz rocznikowo {wiek} lat
Podejrzewam, że jesteś {plec}. Czy zgadłem?"""
)

if plec == "kobietą":
    if wiek < 18:
        print(f"Jeszce nie jesteś pełnoletnia. Brakuje tobie do pełnoletności {18 - wiek} lat.")
    else:
        print(f"Wow jesteś już pełnoletnia od {wiek - 18} lat.")
else:
    if wiek < 18:
        print(f"Jeszce nie jesteś pełnoletni. Brakuje tobie do pełnoletności {18 - wiek} lat.")
    else:
        print(f"Wow jesteś już pełnoletni od {wiek - 18} lat.")
