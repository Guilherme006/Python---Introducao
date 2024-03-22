#if, elif e else

# Exemplo de "if"
idade_01 = 19
print("Exemplo de comando if")
if idade_01 >= 18:
    print("Você é maior de idade")

if idade_01 == 19:
    print("Você tem 19 anos")

if idade_01 < 18:
    print("Você é menor de idade")

if idade_01 != 10:
    print("Você não tem 10 anos")


# Exemplo com "else"
idade_02 = 17
if idade_02 >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")


# Exemplo com "elif"
idade_03 = 16
if idade_03 >= 18:
    print("Você é maior de idade")
elif idade_03 >= 12:
    print("Você é um adolescente")
else:
    print("Você é uma criança")



# Entrada de dados - input
idade = int(input("Digite a sua idade: "))
if idade >= 18:
    print("Você é maior de idade")
elif idade >= 12:
    print("Você é um adolescente")
else:
    print("Você é uma criança")


mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Não pode tirar a carteira de habilitação"
print(mensagem)
