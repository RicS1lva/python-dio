def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("Valor sacado")
        print("Retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f'Depósito efetuado \nSeu saldo é de: R${float(saldo)}')

print("Obrigado por ser nosso cliente, tenha um bom dia!")

sacar(100)
depositar(500)

