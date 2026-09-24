import random

numero_secreto = random.randint(1, 10)
tentativas = 0
acertou = False

print("O computador pensou em um número entre 1 e 10. Tente adivinhar!")

while not acertou:
    chute = int(input("Qual é o seu palpite? "))
    tentativas += 1

    if chute == numero_secreto:
        acertou = True
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
    elif chute < numero_secreto:
        print("Maior... Tente novamente!")
    else:
        print("Menor... Tente novamente!")
