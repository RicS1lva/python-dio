contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

resultado = contatos.popitem()
print(resultado)  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})

resultado = contatos.popitem()
print(resultado)  # KeyError