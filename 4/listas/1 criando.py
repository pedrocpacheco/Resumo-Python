lista = [1, "item 2", 3, ["item 4.1", 4.2]]
# Criando lista

item_1 = lista[0] 
# 0 Index

item_4 = lista[3] 
# Acessando valor que é uma lista, dentro da lista.

item_4_1 = item_4[0]
# Acessando primeiro valor dessa nova lista

item_4_1_direto = lista[3][0]
# Pode ser feito assim também

print(f"Isto {item_4_1} é o mesmo que isso {item_4_1_direto}")
# Resultado -> Isto 4.1 é o mesmo que isso 4.1
