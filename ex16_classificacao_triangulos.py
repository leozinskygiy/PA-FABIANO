a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("É um triângulo EQUILÁTERO.")
    elif a == b or a == c or b == c:
        print("É um triângulo ISÓSCELES.")
    else:
        print("É um triângulo ESCALENO.")
else:
    print("Os segmentos informados não formam um triângulo.")
