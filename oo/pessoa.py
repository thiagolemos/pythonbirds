class Pessoa:
    olhos=2

    def __init__(self, *filhos, nome=None, idade=35 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    thiago = Homem(nome='Thiago')
    marcelo = Mutante(thiago, nome='Marcelo')
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
    print(Pessoa.metodo_estatico(), thiago.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), thiago.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(thiago, Pessoa))
    print(isinstance(thiago,Homem))
    print(thiago.Olhos)





