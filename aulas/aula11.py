num1 = input('Digite um número positivo inteiro: ')
num2 = input('Digite outro número positivo inteiro: ')


# isnumeric checa se é numero e positivo
if(num1.isnumeric() and num2.isnumeric()):
    print(int(num1)+int(num2))
else:
    print('Digite dois número positivos')

# ou

try:
    print(int(num1)+int(num2))
except:
    print('Error')