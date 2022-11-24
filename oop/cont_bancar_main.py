from oop.cont_bancar import ContBancar

cont1 = ContBancar('Ramona G', 'RO001')
cont2 = ContBancar('Alex G', 'RO002')

cont1.activare_cont(7777)
cont2.activare_cont(3333)
cont2.activare_cont(7777)

cont1.alimentare_cont(300)
cont2.alimentare_cont(700)
cont2.alimentare_cont(300)

cont1.plata_card(500)
cont2.plata_card(100)
cont2.plata_card(200)
cont1.plata_card(300)

cont1.interogare_sold()
cont2.interogare_sold()

# tema: Clasa angajat
# nume, prenume, salariu, vechime, functie
# constructor: nume, prenume, salariu, functie, vechime
# metoda1: descriere
# metoda2: actualizare vechime (parametru noua vechime) = self.vechime = noua_vechime
# metoda3: marire salariu in functie de vechime. Daca vechime <5ani, marire 300 lei. >5ani marire 500 lei