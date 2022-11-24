# # # problema cu dalmatienii
# # for i in range(1, 102):
# #     print(f'Dalmatianul numarul {i}')
# #
# # # problema cu dalmatienii - schimbam pasul din 2 in 2. Ultimul parametru/argument din paranteze reprez pasul
# # for i in range(1, 102, 2):
# #     print(f'Dalmatianul numarul {i}')
#
# numere = [3, 7, 10, 20, 30]
# # # parcurgere listei cu for prin intermediul indexului
# # for i in range(0, len(numere)):
# #     print(f'Indexul numarului curent este {i} si valoarea numarului curent este {numere[i]}')
#
# #for each
# for numar in numere:
#     print(f'Numarul curent este {numar}')
#
# # for each - algoritmul cu suma numerelor
# suma = 0
# for numar in numere:
#     suma = suma + numar
# print(f'Suma numerelor este {suma}')

# de cate ori apare 3 in [3, 2, 3, 5, 3, 3]
numere = [3, 2, 3, 5, 3, 3, 9, 20, 3, 15, 3]
aparitii = 0
for numar in numere:
    if numar == 3:
      aparitii = aparitii+1
print(f'Numarul 3 apare de {aparitii} ori')




