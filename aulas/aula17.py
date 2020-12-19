# while/else
x=0
while x < 10:
    print(x)
    x+=1
else:
    print(f'x chegou em {x} e entrou no else')
# o else só executa se a condição do laço for falsa, se tiver um break não entra