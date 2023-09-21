MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade_usuario = int(input("Informe sua idade: "))

if idade_usuario >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
    
if idade_usuario < MAIOR_IDADE:
    print("Ainda não pode tirar CNH")


if idade_usuario >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")


if idade_usuario >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade_usuario == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não pode fazer as aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")