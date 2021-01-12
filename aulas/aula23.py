# desempacotamento de lista
lista = ['João', 'Sebastião', 'Pafuncia', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n1, n2, n3 = lista
# print(n1,n2,n3)




v1, v2, v3, *numeros, ultimovalor = lista
print(v1,v2, v3)
print(numeros)
print(ultimovalor)