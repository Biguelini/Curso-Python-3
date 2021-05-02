import json

# file = open('arquivo.txt', 'w+')
# file.write('Linha1\n')
# file.write('Linha2\n')
# file.write('Linha3\n')
# file.write('Linha4\n')
# file.write('Linha5\n')
# file.close()

d1 = {
    'Pessoa 1':{
        'nome': 'João',
        'sobrenome': 'Biguelini'
    },
    'Pessoa 2':{
        'nome': 'Ana',
        'sobrenome': 'Andrade'
    }
}

d1_json = json.dumps(d1)
with open('arquivo.json', 'w+') as file:
    file.write(d1_json)
print(d1_json)