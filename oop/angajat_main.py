from oop.angajat import Angajat

angajat1 = Angajat('G','Ramona', 'Director', 1000, 3)
angajat2 = Angajat('G', 'Alex', 'manager', 700, 8)
angajat3 = Angajat('I', 'Madalina', 'instructor', 500, 10)

angajat1.actualizare_vechime(6)
angajat2.actualizare_vechime(3)
angajat3.actualizare_vechime(1)

angajat1.marire_salariu()
angajat2.marire_salariu()
angajat3.marire_salariu()

angajat1.descriere()
angajat2.descriere()
angajat3.descriere()