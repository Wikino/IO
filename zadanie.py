from datetime import datetime
dane = input("Podaj swoje imię i nazwisko: ")
imie, nazwisko = dane.split()
rok = input("Podaj swój rok urodzenia: ")
duze_litery= nazwisko.upper()
ile_liter_imie= len(imie)
ile_liter_nazwisko= len(nazwisko)
ile_lat= datetime.now().year-int(rok)
if imie[-1]=="a":
    plec="kobietą"
else:
    plec = "mężczyzną"
tekst = f"Cześć {imie} {duze_litery}! Twój rok urodzenia to {rok}!"
tekst2 = f"Twoje imie ma {ile_liter_imie} liter, a nazwisko {ile_liter_nazwisko}."
tekst3= f"Masz rocznikowo {ile_lat} lat"
tekst4=f"Podejrzewam, że jesteś {plec}. Czy zgadłem?"
print(tekst)
print(tekst2)
print(tekst3)
print(tekst4)
if plec=="kobietą":
    if ile_lat < 18:
        print(f"Jeszce nie jesteś pełnoletnia. Brakuje tobie do pełnoletności {18 - ile_lat} lat.")
    else:
        print(f"Wow jesteś już pełnoletnia od {ile_lat - 18} lat.")
else:
    if ile_lat <18:
        print(f"Jeszce nie jesteś pełnoletni. Brakuje tobie do pełnoletności {18-ile_lat} lat.")
    else:
        print(f"Wow jesteś już pełnoletni od {ile_lat-18} lat.")

