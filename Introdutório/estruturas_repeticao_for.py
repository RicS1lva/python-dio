''' 
texto = input("Informe um texto: ") 
VOGAIS = "AEIOU"

for letra in texto:
	if letra.upper() in VOGAIS: # .upper transforma em maiúsculo
				print(letra, end="")

print() # adiciona uma quebra de linha

for letra in texto:
	if letra.upper() in VOGAIS: # .upper transforma em maiúsculo
				print(letra, end="")

else:
	print() # adiciona uma quebra de linha
	
    '''

for numero in range(0, 51, 5):
	print(numero, end=" ")