nome = "riCaRDo"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   Olá mundo!    "

print(texto)
print("." + texto.strip() + ".")
print("." + texto.lstrip() + ".")
print("." + texto.rstrip() + ".")

menu = "Python"
menu2 = "Java"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print(menu2.center(14, "#"))
print("P-y-t-h-o-n")
print("-".join(menu))

for letra in menu:
    print(letra,end="-")

