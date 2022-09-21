salario= float(input("Digite seu Salario: "))
porcentagem= int(input("Digite a Porcentagem de aumento: "))
#print("Seu Salario e de: %0.2f" %salario)


aumento= float(porcentagem/100)
con= 1 + aumento
ress= con*salario

print("Seu Salario passara para: %0.2f" %ress)