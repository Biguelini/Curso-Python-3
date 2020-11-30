# tipos primitivos 

"""
str - string: textos 'assim' ou "assim"
int - inteiro: números inteiros ex: 123456789 ou -123456789
float - real/ponto flutuante: números com vírgula ex 123.123546 ou -123.45689
bool - booleano/lógico: verdadeiro ou falso True ou False
"""

print(type('João'))
print(type(10))
print(type(1.5))
print(type(True))
#saída: 
"""
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
"""

"""
Converter
str - str(var)
int - int(var) só converte se for float
float - float(var) só converte se for int
bool - bool(var)
"""
# str
print('João', type('João'))
# int
print(15, type(15))
# float
print(1.89, type(1.89))
# bool
print(15>=18, type(15>=18))