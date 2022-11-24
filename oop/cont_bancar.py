class ContBancar:
    # constructor
    def __init__(self, titular_cont, iban):
        # atribute/ field-uri
        self.titular_cont = titular_cont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0

    # interogare sold
    def interogare_sold(self):
        print(f'Titular: {self.titular_cont}')
        print(f'Iban: {self.iban}')
        print(f'Sold: {self.sold}')
        print(f'Status card: {self.activ}')
        print(f'Nr de incercari: {self.incercari_activare}')
        print('--------------------------------')

    def activare_cont(self, pin_utilizator):
        print(f'Buna {self.titular_cont}')
        if pin_utilizator == self.pin:
            print('Card activat cu succes')
            self.activ = True
        else:
            print('PIN gresit!')
            self.incercari_activare = self.incercari_activare + 1
            # sau se poate scrie self.incercari_activare+=1

    def salut(self):
        print(f'Buna {self.titular_cont}')

    def alimentare_cont(self, suma_alimentata):
        self.sold += suma_alimentata
        self.salut()
        print(f'Ati alimentat suma de {suma_alimentata} ')
        print(f'Aveti in cont suma de {self.sold}')

    def plata_card(self, suma_cheltuita):
        # variabile scope
        self.salut()
        if suma_cheltuita <= self.sold:
            self.sold -= suma_cheltuita
            print(f'Ati cheltuit {suma_cheltuita}')
            print(f'Aveti in cont {self.sold}')
        else:
            print('Fonduri insuficiente!')





