jogo_favorito = {
    "nome": "Red Dead Redemption 2",
    "plataforma": "Xbox"
}

print(jogo_favorito)
# Resultado -> {'nome': 'Red Dead Redemption 2', 'plataforma': 'Xbox'}

jogo_favorito.update({"nome":"Cyberpunk 2077", "ano_lancado": "2020"})
# Atualizamos o dicionario mudando o valor de uma chave existente, e criando outra.

print(jogo_favorito)
# Resultado -> {'nome': 'Cyberpunk 2077', 'plataforma': 'Xbox', 'ano_lancado': '2020'}

jogo_favorito.update({"nome": "Tales From the Borderlands",
                      "ano_lancado": "2013", "melhor_musica": "Kiss The Sky"})
# Atualizamos o dicionario mudando 2 valores de chaves existentes, e criando um novo.

print(jogo_favorito)
# Resultado -> {'nome': 'Tales From the Borderlands', 'plataforma': 'Xbox', 'ano_lancado': '2013', 'melhor_musica': 'Kiss The Sky'}
