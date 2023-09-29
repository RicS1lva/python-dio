pessoa = {
    "Nome": "Ricardo",
    "Sobrenome": "da Silva"
}

pessoa.fromkeys(["idade", "email"], "vazio")

pessoa["idade"] = 25
pessoa["carro"] = "celta"

print(pessoa)


print(dict.fromkeys(["nome", "telefone"]))  # {"nome": None, " telefone": None}

print(dict.fromkeys(["Nome", "telefone"], "vazio"))  # {'Nome': 'vazio', 'telefone': 'vazio'}
