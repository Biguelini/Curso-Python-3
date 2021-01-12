# split join enumerate
# string = 'Uma frase qualquer, uma frase bem bonita!'

# lista = string.split(' ')
# lista2 = string.split(',')


# string2 = '-'.join(lista)

lista = ['João', 'Pedro', 'Maria']
# for indice, valor in enumerate(lista):
#     print(indice, valor)


#enumerate faz isso
lista = [
    [0,'João'],
    [1,'Pedro'],
    [2,'Maria']
]
for indice, nome in lista:
    print(indice, nome)

