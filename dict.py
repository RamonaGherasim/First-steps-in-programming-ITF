# declaram si initializam un dict (dictionary)
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}

# adaugam elemente in dict
note_elevi['Sebi'] = 7

# printam dictul
print(note_elevi)

# aflam elemente din dict
print(note_elevi['Gigel'])
# sau putem folosi metda 'get'
print(note_elevi.get('Gigel'))

# actualizam valori
note_elevi['Costel'] = 10
print(note_elevi)

# aflam dimensiunea
print(len(note_elevi))

# stergem valori
note_elevi.pop('Gigel')
print(note_elevi.get('Gigel', 'nu mai avem acest elev'))
print(note_elevi)

# returnam cheile
print(note_elevi.keys())