# função que exibe a saudação
def saudar(nome, saudacao):
    print(f"{saudacao}, {nome}!")
saudar('João', 'Olá')

def somar_tres(n1, n2, n3):
    print(n1+n2+n3)
somar_tres(1,2,5)

def percentual(n, p):
    soma = n + n*(p/100)
    return soma
porcento = percentual(5, 50)
print(porcento)

def fizzbuzz(n):
    if n%5 == 0 and n%3 == 0:
        return "fizz buzz"
    elif n%3 == 0:
        return "fizz"
    elif n%5 == 0:
        return "buzz"
    else:
        return n
fb = fizzbuzz(7)
print(fb)