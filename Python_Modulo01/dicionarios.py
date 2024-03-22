# Criando um dicionário de exemplo
pessoa = {"nome": "Guilherme",
          "idade": 25,
          "cidade": "Curitiba"
        }

print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Lazari"
print("Sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 30
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplo:", pessoa)


# Métodos: keys() - retorna todas as chaves, values() - retorna todos os valores, items() - retorna uma lista de tuplas

# Keys()
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# Values()
valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valor:", valores[0])

# Items()
itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][1]))
