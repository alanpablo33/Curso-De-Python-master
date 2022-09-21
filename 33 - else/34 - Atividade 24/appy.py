num1= int(input("Digite o Primeiro Numero: "))
num2= int(input("Digite o Segundo Numero: "))

ress= num1*num2
print("Resultado de Multiplicação e: %d " %ress)

if ress <= 100:
    print("Numero Baixo")

else:
    print("Numero Alto")