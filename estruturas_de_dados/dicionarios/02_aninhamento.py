contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7776", "extra": {"a": 1}},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # 3443-2121
print(telefone)  # 3443-2121

extra = contatos["melaine@gmail.com"]["extra"]["a"]
print(extra)  # 1