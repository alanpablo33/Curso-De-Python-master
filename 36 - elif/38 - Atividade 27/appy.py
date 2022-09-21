renda= int(input("Digite Sua Renda para que possamos Liberar um limite de Credito para Você: "))
print("Sua Renda e de :%d" %renda)

if renda < 2000:
    print("Limite de 1000 foi Liberado")

elif renda < 4000:
    print("Limite de 2000 foi liberado")

elif renda <= 9000:
    print("Limite de 5000 foi liberado")

elif renda > 10000:
    print("Ir Falar com o Gerente")