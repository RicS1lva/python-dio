def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", 
            combustivel="gasolina") # válido

# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", 
#             combustivel="gasolina") # inválido

""" Keyword and positional Only """

def criar_carros(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carros("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", 
            combustivel="gasolina") # Válido

# criar_carros(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", 
#             combustivel="gasolina") # inválido