# entrada de dados

nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
# idade = int(input('Qual sua idade? '))
nasceu = 2020 - int(idade)
print(f'Legal, {nome}')
print(f'{nome} nasceu em {nasceu}')