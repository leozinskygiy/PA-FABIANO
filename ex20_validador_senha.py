senha_secreta = "etec123"
senha = input("Digite a senha: ")

while senha != senha_secreta:
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")

print("Acesso Permitido")
