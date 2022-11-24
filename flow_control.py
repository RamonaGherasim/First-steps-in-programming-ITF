print('Pornesc radioul')
piesa_faina = False

# Daca ne place piesa dam radioul mai tare
if piesa_faina == True :
    print('Dau radioul mai tare')
    print('Incep sa fredonez piesa')

print('Opresc radioul')

# if else
# daca numarul este par, printam acest lucru.
# altfel, printam impar.
nr = 4
# ce inseamna numar par? => Se imparte exact la 2
# ce inseamna ca se imparte exact la 2? => impartirea da restul 0 => modulus este 0

if nr % 2 == 0:
    print(f'{nr} este un numar par')
else:
    print(f'{nr} este un numar impar')

# este un numar pozitiv?
# ce inseamna numar pozitiv? => nr > 0
if nr > 0:
    print(f'{nr} este un numar pozitiv')
else:
    print(f'{nr} nu este un numar pozitiv')

# # daca utilizaztorul are sub 18 ani, nu poate paria
# varsta = 22
# if varsta < 18:
#     print('Ne pare rau, varsta minima pentru a paria este 18 ani!')
# else:
#     print('Bine ati venit, incepe pariul aici!')
#
# # if, else if, else
# # cum ne saluta robotelul in functie de ora
#
# # luam date de la tastatura si ne asiguram ca sunt tranf din str in int
# ora = int(input('Introduceti ora'))
# if ora < 0:
#     print('ora invalida. ora negativa')
# elif ora <= 11:
#     print('Buna dimineata')
# elif ora <= 18:
#     print('Buna ziua')
# elif ora <= 21:
#     print('Buna seara')
# elif ora <= 24:
#     print('Noapte buna')
# else:
#     print('ora invalida. ora mai mare decat 24')
#
# # v<0 vit invalida, 0 stationare, <=50 localitate, <=90 judetean, altfel autostrada
# viteza = int(input('Introduceti viteza'))
# if viteza < 0:
#     print('Viteza invalida. Va rugam introduceti o valoare pozitiva')
# elif viteza == 0:
#     print('Masina este in stationare')
# elif viteza <= 50:
#     print('Circulati in localitate')
# elif viteza <=90:
#     print('Circulati pe un drum judetean')
# else:
#     print('Circulati pe autostrada')

# CTRL + / pentru a comenta si decomenta mai multe linii de cod (selectati liniile intai)

# robotel telefonic
optiunea = int(input('Alege o optiune'))
if optiunea == 0:
    print('Reveniti la meniul anterior')
elif optiunea == 1:
    print('Ati ales limba romana')
elif optiunea == 2:
    print('Ati ale limba engleza')
else:
    print('Nu am identificat optiunea, mai incearca')