class Pessoa:
    ano = '2020'

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if not(self.comendo):
            print(f'{self.nome} está comendo {alimento}.')
            self.comendo = True
            return
        print(f'{self.nome} já está comendo.')
        return

    def parar_comer(self):
        if not(self.comendo):
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False
        return

    def falar(self, assunto):
        if (self.comendo):
            print(f'{self.nome} não pode falar comendo')
            return
        if not(self.falando):
            print(f'{self.nome} irá falar sobre {assunto}')
            self.falando = True
            return
        print(f'{self.nome} já está falando.')
        return
    def parar_falar(self):
        if(self.falando):
            print(f'{self.nome} irá para de falar')
            self.falando = False
            return
        print(f'{self.nome} não está falando')