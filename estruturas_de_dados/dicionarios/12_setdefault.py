contato = { "nome": "Ricardo", "telefone": "3333 - 2221"}

resultado = contato.setdefault("nome", "Fernanda")
print(resultado)  # Ricardo
print(contato)  # {'nome': 'Ricardo', 'telefone': '3333 - 2221'}

resultado = contato.setdefault("idade", 25)
print(resultado)  # 25
print(contato)  # {'nome': 'Ricardo', 'telefone': '3333 - 2221', 'idade': 25}