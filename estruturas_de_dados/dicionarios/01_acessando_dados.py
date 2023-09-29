dados = {'nome': 'Guilherme', 'idade': 28, 'telefone': '3333 - 1234'}

print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333 - 1234"

dados["nome"] = "Ricardo"
dados["idade"] = 25
dados["telefone"] = "4002 - 8922" 

print(dados)  # {'nome': 'Ricardo', 'idade': 25, 'telefone': '4002 - 8922'}