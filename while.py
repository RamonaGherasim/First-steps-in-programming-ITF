# problema: masina care merge atat timp cat mai are benzina
litri_benzina = 10

while litri_benzina > 0:
    # acceleram
    print('Vroom, vroom!')
    # scadem benzina
    litri_benzina = litri_benzina - 1
    if litri_benzina <= 3:
        print('Se aprinde senzorul de pompa!')
print('STOP! Ai ramas fara benzina!')
