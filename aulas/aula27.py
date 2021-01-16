# funções
# def mostrar():
#     print('Hello World')
# mostrar()


# def mostrar(texto):
#     print(texto)
# mostrar('Hello World')


# def saudacao(msg, nome):
#     print(msg, nome)
# def saudacao(msg = 'Olá', nome = 'usuário'):
#     nome = nome.replace('a', '4')
#     print(msg, nome)

# saudacao('Hello', 'João')
# saudacao('Olá', 'Ana')
# saudacao('Oi', 'Pafuncia')
# saudacao('Eae', 'Pedro')
# saudacao(nome='Zézinho', msg='Hi')
# saudacao()

def saudacao(msg = 'Olá', nome = 'usuário'):
    nome = nome.replace('a', '4')
    return f'{msg}, {nome}'
variavel = saudacao()
print(variavel)