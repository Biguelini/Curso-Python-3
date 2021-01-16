from random import randint

novo_cpf = str(randint(100000000, 999999999))
reverso = 10                        
total = 0

# Loop do CPF
for index in range(19):
    if index > 8:                  
        index -= 9                  
    total += int(novo_cpf[index]) * reverso  

    reverso -= 1                    
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:                   
            d = 0
        total = 0                   
        novo_cpf += str(d)          

sequencia = novo_cpf == str(novo_cpf[0]) * 11

if not sequencia:
    print(novo_cpf)
