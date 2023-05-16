print("Chamando Função antes de Inicializa-la")
funcao_tardia()

# Isso funciona? | NÃO!
# Pois, no momento que chamamos a funcao_tardia, ela não foi definida

def funcao_tardia():
    print("Me definiram depois de me chamar")

def funcao_tres():
    funcao_um()
    funcao_dois()
    print("3")

def funcao_dois():
    funcao_um()
    print("1")

def funcao_um():
    print("1")

funcao_tres()

# Isso funciona? | SIM!
# Pois no momento que chamamos a funcao_tres, a 1 e a 2 ja foram declaradas