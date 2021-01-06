# listas em python 
# fatiamento 
# append, insert, pop, del, clear, extend, +
# min, max
# range
lista =  ['l', 'i','s','t','a',1]
# print(lista[::2])
# l1 = [1,2,3]
# l2 = [4,5,6]

l1 = list(range(1, 4))
l2 = list(range(4, 7))

# l1.extend(l2) 
# l1.extend('a') [1, 2, 3, 4, 5, 6, 'a']
# l1.append(l2) 
# l1.append('b') [1, 2, 3, [4, 5, 6], 'b']
# l2.insert(0, 'bacon') ['bacon', 4, 5, 6]
# l2.pop() ['bacon', 4, 5]
# del(l2[1:3]) ['bacon', 6]

for valor in l2:
    print(valor)
# print(max(l1))
# print(min(l1))
# print(max(l2))
# print(min(l2))
print(l1)
print(l2)


secreto = 'baconzitos'
digitadas = []
vidas = 3
while True:
    if vidas <= 0:
        print('Você perdeu! :(')
        break
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
    
    if letra in secreto:
        print(f'UHUUUUUUUULLLLLL, a letra "{letra} existe na palavra secreta."')
        digitadas.append(letra)
    else:
        print(f'AFFFFFFF, a letra {letra} NÃO EXISTE na palavra secreta.')
        vidas -= 1
        print(f'Você ainda tem {vidas} vidas')
    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'
    if secreto_temp == secreto:
        print('Você ganhou! :)')
        break
    else:
        print(f'A palavra secreta está assim {secreto_temp}')