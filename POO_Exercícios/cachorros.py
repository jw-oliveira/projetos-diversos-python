class Cachorro:
    def __init__(self, nome, raca, peso, cor):
        self.nome = nome
        self.raca = raca
        self.peso = peso
        self.cor = cor

    def latir(self):        
        return "Au-Au"

    def apresentar(self):
        print(f"Olá meu nome é {self.nome}, sou da raça {self.raca}, peso {self.peso}Kg e sou da cor {self.cor}.")

    def mudarNome(self, novo_nome):
        self.nome = novo_nome

    def cadastraCachorro(nome, raca, peso, cor):
        cachorros.append((Cachorro(nome, raca, peso, cor)))      


cachorros = [(Cachorro("Toby", "Boxer", 30, "Marrom")), (Cachorro("Lupy", "Golden", 25, "Preto"))]


nome = str(input('Nome: '))
raca = str(input('Raça: '))
peso = float(input('Peso: '))
cor = str(input('Cor: '))

Cachorro.cadastraCachorro(nome, raca, peso, cor)

cachorros[2].apresentar()

cachorro1 = Cachorro("Toby", "Boxer", 30, "Marrom")
cachorro2 = Cachorro("Lupy", "Golden", 25, "Preto")

cachorro2.apresentar()
cachorro2.mudarNome("Lulu")
cachorro2.apresentar()
