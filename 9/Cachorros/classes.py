class Cachorro:
    total = 0

    def __init__(self, nome, idade, apelido):
        self.nome = nome
        self.idade = idade
        self.apelido = apelido
        Cachorro.total += 1
    
    def to_string(self):
        return f"Cachorro {self.nome} com {self.idade} anos e apelido {self.apelido}"

    def latir(self, latido="Wer Wer"):
        print(f"{self.nome}: {latido}")

lully = Cachorro("Lully", 3, "Lulleca")
try:
    print(f"A {lully.nome} é a nossa cachorrinha, ela tem {lully.idade} anos. E é a nossa {lully.total} cachorra")
except AttributeError:
    print("Nome e Idade são de uma instância, não da classe.")

# 1 ano se passa
lully.idade = 4
print(f"Agora a {lully.nome} tem: {lully.idade} anos de idade")

lully.latir()

class ViraLata(Cachorro):
    def __init__(self, nome, idade, apelido, tamanho_dentes):
        super().__init__(nome, idade, apelido)
        self.tamanho_dentes = tamanho_dentes
    
    def to_string(self):
        return super().to_string() + f"e tamanho de dentes de {self.tamanho_dentes}"
    
    def latir(self, latido="Au au"):
        return super().latir(latido)

caramelo = ViraLata("Caramelo", 4, "Caca", 50)
print(lully.to_string())
print(caramelo.to_string())

print(lully.latir())
print(caramelo.latir())

print(type(lully))
print(type(caramelo))

print(isinstance(lully, ViraLata))
print(isinstance(caramelo, Cachorro))