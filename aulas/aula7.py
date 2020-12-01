# formatação de strings
var = 'isto é uma var'
arrendondar = 2.15546123465465463215646156456163
formatar = '.format()'
print(f'Formatando strings {var} e posso colocar var dentro do print mais fácil')
print(f'Consigo determinar as casas decimais que aparecerão assim {arrendondar:.2f}')
print('Posso usar o {} também'.format(formatar))
print('Posso usar o {f} também'.format(f=formatar))