contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7776"},
}


for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

  # guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2221'}
  # giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3443-2121'}
  # chappie@gmail.com {'nome': 'chappie', 'telefone': '3344-9871'}
  # melaine@gmail.com {'nome': 'Melaine', 'telefone': '3333-7776