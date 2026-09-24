idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("Não vota.")
elif (16 <= idade <= 17) or (idade > 65):
    print("Voto facultativo.")
else:
    print("Voto obrigatório.")
