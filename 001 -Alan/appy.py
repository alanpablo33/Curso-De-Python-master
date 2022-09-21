#calculadora


num1= int(input("Digite primeiro numero:"))
num2= int(input("Digite o segundo numero:"))
operador = input("Digite o operador para ser solucionado: ")
ress= "  "

if operador in "-":
    ress = num1 - num2
    print(ress)

elif operador in "+":
    ress = num1 + num2
    print(ress)

elif operador in "/":
    ress = num1 / num2
    print(ress)

elif operador in "*":
    ress = num1 * num2
    print(ress)



else:
    print("Digite corretamente para usar a calculadora")
