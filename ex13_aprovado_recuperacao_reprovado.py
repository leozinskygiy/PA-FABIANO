n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2

if media >= 7.0:
    print(f"Média {media:.1f}: APROVADO")
elif 5.0 <= media < 7.0:
    print(f"Média {media:.1f}: RECUPERAÇÃO")
else:
    print(f"Média {media:.1f}: REPROVADO")
