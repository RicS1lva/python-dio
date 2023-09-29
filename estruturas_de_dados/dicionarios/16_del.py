contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7776"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

print(contatos)
  # {'guilherme@gmail.com': {'nome': 'Guilherme'}, 
  # 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 
  # 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7776'}}