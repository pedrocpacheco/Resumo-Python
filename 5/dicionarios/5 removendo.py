personagem = {"nome": "Arthur Morgan", "idade": "36", "jogo": "Red Dead Redemption 2"}
print(personagem)
# {'nome': 'Arthur Morgan', 'idade': '36', 'jogo': 'Red Dead Redemption 2'}

del personagem["jogo"] # Deletando chave e valor de jogo
print(personagem)
# {'nome': 'Arthur Morgan', 'idade': '36'}

idade_removida = personagem.pop("idade") # Chave a ser removida e retornada entre ()
print(personagem)
# {'nome': 'Arthur Morgan'}

print(idade_removida)
# 36
