print("For utilizando tupla")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)


print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)


pessoa = {"nome": "Guilherme", "idade": 25, "cidade": "Curitiba"}
print("For utilizando dicionario - chaves")
for chave in pessoa.keys():
    print(chave)

print("For utilizando dicionario - valores")
for valor in pessoa.values():
    print(valor)

print("For utilizando dicionario - itens")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


# range() = intervalo numérico
# [0, 1, 2, 3, 4]
print("Utilizando a funcao range()")
for numero in range(5):
    print("Numero:", numero)


print("Utilizando a funcao range() com len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)


# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
