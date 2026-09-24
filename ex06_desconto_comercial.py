valor_original = float(input("Digite o valor original do produto (R$): "))
desconto = valor_original * 0.15
valor_final = valor_original - desconto

print(f"Valor com 15% de desconto: R$ {valor_final:.2f}")
