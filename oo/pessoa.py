class Pessoa:
    olhos=2

    def __init__(self, *filhos, nome=None, idade=35 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    thiago = Pessoa(nome='Thiago')
    marcelo = Pessoa(thiago, nome='Marcelo')
    print(Pessoa.cumprimentar(marcelo))
    print(id(marcelo))
    print(marcelo.cumprimentar())
    print(marcelo.nome)
    print(marcelo.idade)
    for filho in marcelo.filhos:
        print(filho.nome)
    marcelo.sobrenome='Lemos'
    del marcelo.filhos
    print(marcelo.__dict__)
    print(thiago.__dict__)
    print(marcelo.olhos)
    print(thiago.olhos)



