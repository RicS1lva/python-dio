nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade)
print("teste", end=" ")
print(nome, idade, end="...\n") #\n é a quebra de linha.
print(nome, idade, sep="#", end="...\n")
print(nome, idade, sep="#")
