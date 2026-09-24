maior = None
menor = None

for i in range(1, 6):
    num = int(input(f"Digite o {i}º número: "))
    if i == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f"Maior valor digitado: {maior}")
print(f"Menor valor digitado: {menor}")
