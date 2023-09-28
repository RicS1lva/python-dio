numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
		if numero % 2 == 0:
				pares.append(numero)
				
numeros2 = [1, 30, 21, 2, 9, 65, 34]
pares2 = [numero for numero in numeros2 if numero % 2 == 0]
		#		retorno        iteração            checagem    


numeros3 = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros3:
		quadrado.append(numero ** 2)
		
numeros4 = [1, 30, 21, 2, 9, 65, 34]
quadrado2 = [numero ** 2 for numero in numeros4]

print(pares)
print(pares2)
print(quadrado)
print(quadrado2)