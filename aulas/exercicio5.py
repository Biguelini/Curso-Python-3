

def add_tarefa(tarefas, tarefa):
    tarefas.append(tarefa)


def remove_tarefa(tarefas):
    tarefas.pop()


def mostra_tarefas(tarefas):
    for tarefa in tarefas:
        print(tarefa)


def main():
    tarefas = []
    ultima_acao = ''
    removida = ''
    desfez = False
    while True:
        print('---Lista de tarefas---')
        print(
            '[1] inserir tarefa\n[2] listar tarefas\n[3] desfazer ação\n[4] refazer ação\n[0] sair')
        op = int(input())
        if(op == 0):
            break
        elif(op == 1):
            ultima_acao = 'add'
            removida = str(input())
            add_tarefa(tarefas, removida)

        elif(op == 2):
            mostra_tarefas(tarefas)
        elif(op == 3 and ultima_acao == 'add'):
            ultima_acao = 'undo'
            remove_tarefa(tarefas)
            print('Ação desfeita')
        elif(op == 4 and ultima_acao == 'undo'):
            add_tarefa(tarefas, removida)
            print('Ação refeita')
main()