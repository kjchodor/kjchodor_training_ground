import random

liczba_do_zgadniecia = random.randint(100,999)
liczba_do_zgadniecia = str(liczba_do_zgadniecia)

def czy_dluzsze_niz(tablica, maksymalna_dlugosc):
    if len(tablica) > maksymalna_dlugosc:
        return True
    else:
        return False

def jest_liczba(liczba_podana):
    for x in liczba_podana:
        if x not in "0123456789":
            return False
    return True

while True:
    porazka = 0
    print("podaj liczbe:")
    liczba_podana = input()
    if liczba_podana == liczba_do_zgadniecia:
        print("brawo")
        print("koniec")
        exit()

    if jest_liczba(liczba_podana) == False:
        print("nie liczba")
        continue

    if len(liczba_podana) < 3:
        print("za mala liczba")
        continue

    jest_dluzsza_niz_3 = czy_dluzsze_niz(liczba_podana, 3)
    if jest_dluzsza_niz_3:
        continue

    if liczba_podana[0] == liczba_do_zgadniecia[0]:
        print("fermi")
    elif liczba_podana[0] == liczba_do_zgadniecia[1] or liczba_podana[0] == liczba_do_zgadniecia[2]:
        print("piko")
    else:
        porazka = porazka + 1

    if liczba_podana[1] == liczba_do_zgadniecia[1]:
        print("fermi")
    elif liczba_podana[1] == liczba_do_zgadniecia[0] or liczba_podana[1] == liczba_do_zgadniecia[2]:
        print("piko")
    else:
        porazka = porazka + 1

    if liczba_podana[2] == liczba_do_zgadniecia[2]:
        print("fermi")
    elif liczba_podana[2] == liczba_do_zgadniecia[1] or liczba_podana[2] == liczba_do_zgadniecia[0]:
        print("piko")
    else:
        porazka = porazka + 1

    if porazka == 3:
        print("bajgle")
