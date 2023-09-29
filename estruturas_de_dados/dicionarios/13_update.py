contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

resultado = contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)
  # {'guilherme@gmail.com': {'nome': 'Gui'}}
resultado = contatos.update({"gioanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
print(contatos)
  # {'guilherme@gmail.com': {'nome': 'Gui'}, 'gioanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}