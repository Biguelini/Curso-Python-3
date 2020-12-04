texto = 'Python_S2'
#indice [012345678]
#indice-[987654321]
print(texto[8])
print(texto[-1])

nova_string = texto[2:6]
print(nova_string)
Python = texto[:6]
print(Python)
s2 = texto[7:]
print(s2)
Python_negativo=texto[-9:-3]
print(Python_negativo)
dois_em_dois=texto[:6:2]
print(dois_em_dois)
tres_em_tres=texto[::3]
print(tres_em_tres)

for letra in texto:
    print(letra)