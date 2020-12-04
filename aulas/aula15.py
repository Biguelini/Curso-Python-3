# while
x=0
while(x<100):
    print(x)
    x+=1


x=0
while(x<100):
    if(x==3):
        print(x)
        break
    print(x)
    x+=1
print('acabou')

while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    op = input('Digite um operador: ')
    
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número!')
        continue
    else:
        if op == '+':
            print(int(num_1)+int(num_2))
        if op == '-':
            print(int(num_1)-int(num_2))
        if op == '*':
            print(int(num_1)*int(num_2))
        if op == '/':
            if(int(num_2)!=0):
                print(int(num_1)/int(num_2))
            else:
                print('O num_2 precisa ser diferente de 0')
        sair = input('Deseja sair? [s]im [n]ão ')
        if(sair=='s'):
            break