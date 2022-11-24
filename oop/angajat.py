class Angajat:
    #constructor
    def __init__(self, nume, prenume, functie, salariu, vechime):
        #fields
        self.nume = nume
        self.prenume = prenume
        self.functie = functie
        self.salariu = salariu
        self.vechime = vechime

    # metoda 1: descriere
    def descriere(self):
        print(f'Numele angajatului: {self.nume}')
        print(f'Preumele angajatului: {self.prenume}')
        print(f'Functia angajatului: {self.functie}')
        print(f'Saariul angajatului: {self.salariu}')
        print(f'Vechimea angajatului: {self.vechime}')
        print('-------------------------------------')

    #metoda 2: actualizare vechime
    def actualizare_vechime (self, noua_vechime):
        self.vechime = noua_vechime

    #metoda 3: marire salariu in functie de vechime. Daca vechime <5ani, marire 300 lei. >5ani marire 500 lei
    def marire_salariu(self):
        if self.vechime < 5:
            self.salariu += 300
            print(f'A primit o marime de salariu in valoare de 300 lei. Noul salariu este {self.salariu}')
        else:
            self.salariu += 500
            print(f'A primit o marime de salariu in valoare de 500 lei. Noul salariu este {self.salariu}')