frase = 'o rato roeu a roupa do rei de Roma'
tamanho_frase = len(frase)
print(tamanho_frase)

contador = 0
nova_string = ''

while contador<tamanho_frase:
    # print(frase[contador], contador)
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    contador+=1
    print(nova_string)