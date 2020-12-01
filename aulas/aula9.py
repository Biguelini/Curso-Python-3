# condições

if (1+1==2):
    print('1+1 é 2')
elif (1+1==11):
    print('1+1 é 11')
else:
    print('Se não for nada')

"""
if - se
elif - se não se 
else - se não
"""

"""
== igual
!= diferente
<= menor ou igual
>= maior ou igual
< menor
> maior
and e
or ou
not não - inversor
in em
not in não em
"""

if(2<3):
    print('2 é menor que 3')
else:
    print('2 não é menor que 3')

if(2<3 and 4>3):
    print('3 entá entre 2 e 3')
else:
    print('3 não está entre 2 e 3')

a = 2
b = 3
if(b>a):
    print('b é maior que a')
else:
    print('b é menor que a')
# retorna 'b é maior que a'

if(not b>a):
    print('b é maior que a')
else:
    print('b é menor que a')
# retorna 'b é menor que a'

v = ''
if(not v):
    print('Preencha o valor de V')
# retorna Preencha o valor de V
if(v):
    print('Preencha o valor de V')
# retorna nada

nome = 'João'
if('o' in nome):
    print(f'Existe a letra O no nome {nome}')
if('v' not in nome):
    print(f'Não existe a letra V no nome {nome}')

# login
usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')
usuario_bd = 'joao'
senha_bd = '123'
if(usuario == usuario_bd and senha == senha_bd):
    print('Logado')
else:
    print('Senha ou usuário incorretos')