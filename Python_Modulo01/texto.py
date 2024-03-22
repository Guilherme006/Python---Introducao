# declaracao
nome_completo = "Guilherme Lazari"

nome_completo_aspas = """"Guilherme
Lazari"""

nome_colpeto_quebra = "Guilherme \
Lazari" 

nome = "Guilherme"
sobrenome = "Lazari"


# formatacao
print("Nome completo (1ª Forma):", nome_completo)
print("Nome completo (2ª Forma):" + nome_completo)
print("Nome completo (3ª Forma):" + "Guilherme" + "Lazari")
print("Nome completo (4ª Forma):" + "Guilherme", "Lazari")
print("Nome completo (5ª Forma):", nome_completo_aspas)
print("Nome completo (6ª Forma):", nome_colpeto_quebra)
print("Nome completo (7ª Forma): %s" % nome_completo)
print("Nome completo (8ª Forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9ª Forma): {nome} {sobrenome}")
print("Nome completo (10ª Forma): {} {}".format(nome, sobrenome))
print("Nome completo (11ª Forma):", nome, sobrenome)

# count() = contar
# find() = achar
# encode() = trasnformar em Byte
# replace() = susbtituicao - Ex: nome.replace("a", "b") = substituiu na variavel nome "a" letra a pela letra "b"
# join() = adciona um separador
# split() = divide uma string em lista
# strip() = remover o que está no início e final de uma string  