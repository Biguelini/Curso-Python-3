# while em python

# while True:
#     nome = input('Qual seu nome?')
#     print(f'Olá {nome}')
# print('Acabou')

x = 0
# while x < 100:
#     print(x)
#     x+=1
#! de 0 a 99
# x = 0
# while x < 100:
#     x+=1
#     print(x)
#! de 1 a 100
# while x < 100:
#     if x == 3:
#         break
#         # break para o codigo
#     print(x)
#     x+=1
x = 0
# while x<=10:
#     y = 0
#     while y<=5:
#         print(f'({x},{y})')
#         y+=1
#     x+=1
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num_1.isnumeric() or num_2.isnumeric():
        print('Digite um número válido')
        continue
    else:
        num_1 = int(num_1)
        num_2 = int(num_2)
        if operador == '+':
            print(num_1 + num_2)
        elif operador == '-':
            print(num_1 - num_2)
        elif operador == '*':
            print(num_1 * num_2)
        elif operador == '/':
            print(num_1 / num_2)
    sair = input('Deseja sair? (S)im (N)ão ')
    if sair == 'S':
        break