# 1
numero = input('Digite um número inteiro ')
if numero.isdigit():
    if int(numero)%2==0:
        print('É par')
    else:
        print('É ímpar')
else:
    print('Digite um número inteiro')

# 2
from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_atuais = int(data_e_hora_atuais.strftime('%H'))
if(data_e_hora_atuais>=0 and data_e_hora_atuais<=11):
    print('Bom dia')
elif(data_e_hora_atuais>=12 and data_e_hora_atuais<=17):
    print('Boa tarde')
else:
    print('Boa noite')

# 3
nome = input('Qual seu primeiro nome? ')
if(len(nome) == 4):
    print('Seu nome é curto')
elif(len(nome) == 4 or len(nome) == 5):
    print('Seu nome é normal')
else:
    print('Seu nome é longo')