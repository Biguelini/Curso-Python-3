perguntas = {
    'Pergunta 1':{
        'pergunta':'Quanto é 2+2',
        'respostas':{'a':'1','b':'2','c':'4'},
        'resposta_certa':'c'
    },
    'Pergunta 2':{
        'pergunta':'Quanto é 5+2',
        'respostas':{'a':'1','b':'7','c':'4'},
        'resposta_certa':'b'
    },
    'Pergunta 3':{
        'pergunta':'Quanto é 2+7',
        'respostas':{'a':'9','b':'2','c':'4'},
        'resposta_certa':'a'
    },
    'Pergunta 4':{
        'pergunta':'Quanto é 2+1',
        'respostas':{'a':'1','b':'3','c':'9'},
        'resposta_certa':'b'
    },
}

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pv['resposta_certa']:
        print('Resposta certa')
        respostas_certas += 1
    else:
        print(f'Resposta errada, a certa era a {pv["resposta_certa"]}')
    print()
qtd_perguntas = len(perguntas)
pct_acerto = respostas_certas/qtd_perguntas*100
print(f'Você acertou {respostas_certas} respostas.')
print(f'Porcentagem de acerto {pct_acerto}%.')