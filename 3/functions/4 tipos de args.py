# Argumentos Posicionais
# Quando passamos os seus valores apenas pelas suas posições

def calcular_total_produto(preco, quantidade):
    resultado = preco * quantidade
    print(resultado)

calcular_total_produto(10, 5)
# Explicação -> Passamos os valores na ordem que eles foram definidos
# ----------------------------------------------------------------------

# Argumentos Nomeados
# Quando passamos os seus valores atraves do seus nomes definidos na função
def mostrar_jogo(nome, ano_lancamento):
    print(f"O Jogo {nome} lançou no ano {ano_lancamento}")

mostrar_jogo(nome="Red Dead Redemption 2", ano_lancamento="2018")
# Explicação -> Aqui, explicitamos de qual argumento tal valor se refere

# ----------------------------------------------------------------------

# Argumentos Padrões
# Argumentos que já possuem um valor pré estabelecido

def infos_aluno(nome, unidade, faculdade="FIAP"):
    print(f"O Aluno {nome} estuda na unidade {unidade} da {faculdade}")

infos_aluno("Pedro", "Paulista")
# Explicação -> Não precisamos passar o argumento faculdade, pois ele ja tem valor.

