aluno = {"first_name": "pedro"}

nome_aluno = aluno["first_name"] 
# Podemos salvar o valor de uma chave assim

sobrenome_aluno = aluno["last_name"]
# Isso da erro, pois não temos uma chave last_name no dic

print(f"Este é o nome do aluno {nome_aluno}")
