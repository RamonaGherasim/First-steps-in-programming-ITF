'''
Operatori:
artitmetici: +, -, *, /, % (modulo, aflarea restului unei impartiri)
de comparare: < >, == , !=, <=, >=
logici: and, or, ! (not)
'''

a = 3
b = 5

print(a + b) # 3+5 => 8
print(a - b) # 3-5 => -2
print(a * b) # 3*5 => 15
print(a / b) # 3/5 => 0.6
print(a % b) # 3%5 => 3

print(a == b) # 3=5? => False
print(a != b) # 3 diferit de 5? => True
print(a < b) # 3<5? => True
print(a <= b) # 3<=5? => True
print(a > b) # 3>5? => False
print(a >= b) # 3>=5? => False

print(a < b and a < 4) # 3<5 SI 3<4? => True SI True => True raspuns final.
print(a < b or a < 2) # 3<5 SAU 3<2? => True SI False => True raspuns final.

# La sedinta cu parintii pot veni: mama sau tata sau (bunicu si bunica).
mama = False
tata = True
bunicu = False
bunica = False
print(mama or tata or (bunicu and bunica)) # => True

mama = False
tata = False
bunicu = False
bunica = True
print(mama or tata or (bunicu and bunica)) # => False

mama = False
tata = False
bunicu = True
bunica = True
print (mama or tata or (bunicu and bunica)) # => True




