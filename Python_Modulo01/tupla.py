# Tupla não pode ser modificada

minha_tupla = (1, 2, 2, 3, 4)
print("Minha tupla:", minha_tupla)

print("Minha tupla[0]:", minha_tupla[0])
print("Minha tupla[2]:", minha_tupla[2])
print("Minha tupla[-1]:", minha_tupla[-1])

# Método count: quantas vezes o elemento aparece
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

indice = minha_tupla.index(2)
print("Indice da primeira ocorrência do elemento 2:", indice)