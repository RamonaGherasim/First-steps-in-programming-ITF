# Ce e o variabila?
# Variabila = Zona din memoria unui calculator care tine diferite date
# Variabila = O cutiuta in care punem diferite valori

# Am declarat si initializat variabila marca
marca_masina = 'Volvo'
# Am declarat si initializat variabila model.
model_masina = 'XC 60'

# loosly typed - nu trebuie sa specificam tipul variabilelor cu care lucram

# Daca vrem sa folosim 2 cuvinte pentu numele variabilei vom folosi tehnica snake e.g. model_masina.
# nu putem folosi spatiu in numele vafriabilei!
# o variabila incepe cu litera mica!

# print (f ' ') este sintaxa in Python entru functia print. f reprezinta format string
print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este modelul: {model_masina}')

# suprascrierea variabilei/ Override
model_masina = 'XC 60 facelift'
print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este modelul: {model_masina}')

# concatnare de stringuri si integere
prenume = 'Ramona'
nume = 'Gherasim'
varsta = 30

print(f'{prenume} {nume} cu varsta de {varsta} ani.')

