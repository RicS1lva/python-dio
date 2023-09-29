contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

copia = contatos.copy()
copia["guilherme@gmai.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])
  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(copia["guilherme@gmai.com"])
  # {'nome': 'Gui'}

copia2 = contatos.copy()
copia2["guilherme@gmail.com"]["nome"] = "Gui"

print(copia2)
  # {'guilherme@gmail.com': {'nome': 'Gui', 'telefone': '3333-2221'}}
print(copia2["guilherme@gmail.com"])
  # {'nome': 'Gui', 'telefone': '3333-2221'}