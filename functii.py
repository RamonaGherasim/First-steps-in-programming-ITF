# functia e scrisa ca def
def printGreeting():
    print('Buna ziua. Bine ati venit!')

def printGreetingByName(nume, prenume):
    print(f'Buna ziua {prenume} {nume}. Bine ati venit!')

def mediaNr(a, b, c):
    return (a+b+c)/3

def piValue():
    return 3.14
    print('abc') # => aceasta linie de cod nu se va rula. Return este ultima instructiune care se executa intr-o
                 # functie. Codul ce vrem sa fie rulat trebuie scris deasupra return-ului

# 1. Aria unui dreptunghi
def ariaDreptunghi(lungime, latime):
    return lungime*latime

# 2. Aria unui cerc
def ariaCerc(raza):
    pi = 3.14
    return pi*raza*raza

# 3. Suma a 2 nr
def sumaNr(a, b):
    return a+b

# 4. o f care returneaza cate caractere are numele + prenumele. Foloseste length for string
def caractereNumePrenume (nume, prenume):
    caractereNume = len(nume)
    caracterPrenume = len(prenume)
    return caractereNume+caracterPrenume

# exercitiu
# daca persoana e majora returnati true, altfel false
def verificareMajor(varsta): # situatie in care puem ave 2 instructiuni de return, dar doar pt ca doar una va fi executata, niciodata ambele
    if varsta >= 18:
        return True
    else:
        return False

# avand 3 numere, returnati pe cel mai  mare
def maxNumar(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# zona de apelare (desktop)
printGreeting()
printGreeting()
printGreetingByName('Gherasim', 'Ramona')
printGreetingByName('Goghie', 'Alex')
printGreetingByName('Istrati', 'Madalina')
print(mediaNr(3, 3, 4))
print(piValue())
print(f'Aria dreptunghiului este: {ariaDreptunghi(3,5)}')
print(f'Aria cercului este: {ariaCerc(3)}')
print(f'Suma numerelor este: {sumaNr(10, 4)}')
print(caractereNumePrenume('Ra', 'Ghe'))
print(verificareMajor(18))
print(f'Numarul cel mai mare este {maxNumar(12, 12, 5)}')

# se ia varsta utilizatorului
age = int(input('Introduceti varsta dvs'))
if verificareMajor(age):#== True
    print('Cont creat, bine ai venit in aplicatie!')
else:
    print('Nu ai varsta minima necesara (18) pentru a paria!')

#oop
# variabile in contextul oop => atribute, proprietati sau fields
# functii in contextul oop   => metode




