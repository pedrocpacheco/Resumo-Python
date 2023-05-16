lista = [1, 2, 3, 4, 5]
# Criando Lista

lista.append(6)
print(lista) # Resultado -> [1, 2, 3, 4, 5, 6]
# Adiona 6 no final da lista

lista.remove(1)
print(lista) # Resultado -> [2, 3, 4, 5, 6]
# Remove o valor passado

lista.insert(0, 9) 
print(lista) # Resultado -> [9, 2, 3, 4, 5, 6]
# Adiciona o valor (9) no index informado (0)

ultimo_valor = lista.pop() 
print(lista) # Resultado -> [9, 2, 3, 4, 5]
print(ultimo_valor) # Resultado -> 6
# remove e retorna o ultimo valor da lista