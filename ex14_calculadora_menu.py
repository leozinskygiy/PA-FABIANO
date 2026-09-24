n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Opção: "))

if opcao == 1:
    print(f"Resultado: {n1 + n2}")
elif opcao == 2:
    print(f"Resultado: {n1 - n2}")
elif opcao == 3:
    print(f"Resultado: {n1 * n2}")
elif opcao == 4:
    if n2 != 0:
        print(f"Resultado: {n1 / n2}")
    else:
        print("Erro: Divisão por zero não permitida.")
else:
    print("Opção inválida.")
