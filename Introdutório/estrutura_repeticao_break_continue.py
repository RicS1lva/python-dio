'''
opcao = -1

while opcao != 0:
		opcao = int(input("Informe um número: "))

		if (opcao % 2) != 0:
				break

		print(opcao)
'''

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 ==0:
        continue
    

    print(numero)

for numero in range(10):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")