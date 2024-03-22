# Declaracao

minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a lista completa
print("Minha lista de exemplo", minha_lista)

# Exibindo elementos da lista
minha_lista[0] = "Python"
print("Minha lista de exemplo", minha_lista)

print(minha_lista[0])
print(minha_lista[5])
print(minha_lista[1:7])
print(minha_lista[:6])
print(minha_lista[2:])


# MÉTODOS DE LISTA

# Método append(): Adiciona elemento no final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# Método index
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# Método insert: insere um elemento em um índice específico 
minha_lista.insert(2, 10)
print("Após o insert(2, 10):", minha_lista)

# Método pop
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", minha_lista)

# Método remove
minha_lista.remove(True)
print("Após o remove(True):", minha_lista)

# Método sort: organiza a lista em ordem crescente
nova_lista = [20, 359, 18, 235, 9]
nova_lista.sort()
print("Após o sort():", nova_lista)