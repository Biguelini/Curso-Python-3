def func1(func2):
    return func2()
def hello():
    return 'Olá, mundo'
print(func1(hello))

def func_mestre(f, *args, **kwargs):
    return f(*args, **kwargs)

def fala_oi(nome):
    return f'Oi, {nome}'

def fala(saud, nome):
    return f'{saud}, {nome}'
print(func_mestre(fala_oi, 'João'))
print(func_mestre(fala, 'Olá', 'João'))