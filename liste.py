# listele in Python pot sa cuprinda elemente de tipuri diferite
# au dimensiune dinamica
fructe = ['mar', 'banana', 'portocala', 3, True, 3]

# afisam o lista
print(fructe)

# accesam un element in functie de index
print(fructe[2])

# adaugam un element nou
fructe.append("rosie")
print(fructe)

# suprascriem un element
fructe[0] = "para"
print(fructe)

# aflam dimensiunea
print(len(fructe))

# scoate si ne returneaza ultimul element
last = fructe.pop()
print('Ultimul element: ', last)
print('Noua lista: ', fructe)

# de cate ori apare un element in lista
print(f'3 apare de {fructe.count(3)} ori in lista')

# extindem lista cu o alta lista
fructe_exoticce = {'ananas', 'kiwi'}
fructe.extend(fructe_exoticce)
print(fructe)
