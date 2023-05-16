frase_alfabeto = "The quick brown fox jumps over the lazy dog"


print(frase_alfabeto[0]) # -> Primeiro Caractere
print(frase_alfabeto[5:]) # -> Mostra a partir do caractere de indice 5 (5 + 1 -> 6)
print(frase_alfabeto[:5]) # -> Mostra só até o caractere de indice 5
print(frase_alfabeto[7:10]) # -> Mostra a partir do indice 7 ao indice 9 (10 n mostra)
print(frase_alfabeto[1:10:2]) # -> Mostra do indice 1 ao 10, pulando de 2 em 2

# string[inicio:final:intervalo]
# inicio -> onde começa
# final -> onde termina (não é mostrado)
# intervalo -> quantos passos para cada iteração

# Também pode ser negativo, ai o sentido é o contrario.
print(frase_alfabeto[1:10:1])
print(frase_alfabeto[10:1:-1])

numeros = [1, 2, 3, 4, 5, 6]
numeros = numeros[1:5:2]

for numero in numeros:
    if numero % 2 == 0:
        print(numero)