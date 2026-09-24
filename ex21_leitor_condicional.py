quantidade = 0
soma = 0

while True:
    num = int(input("Digite um número inteiro (0 para parar): "))
    if num == 0:
        break
    soma += num
    quantidade += 1

print(f"Quantidade de números digitados: {quantidade}")
print(f"Soma dos números: {soma}")
