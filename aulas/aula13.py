# formatação de valores
"""
:s - texto
:d - int
:f - float
:.(numero)f - quantidade de casas decimais
:(caractere)(> ou < ou ^)(quatidade)(tipo - s, d ou f)
> - Esquerda
< - Direita
^ - Centro
"""
num = 1
print(f'{num:0>10}')
print(f'{num:0<10}')
print(f'{num:j<10}')

num_2 = 123456
print(f'{num_2:0^10}')

nome = 'João'
print(f'{nome:#^50}')

print(nome.lower())
print(nome.upper())
print(nome.title())