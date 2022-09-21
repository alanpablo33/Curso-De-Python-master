# caixa eletronico

#Digite um valor
saque = int(input("Digite um valor: "))
print("Valor digitado %d" %saque)

#variaves Notas
nota_100= 0
nota_50= 0
nota_20= 0
nota_10= 0
nota_1= 0

while saque > 0: # se o saque for maior que 0 então
    while saque >= 100: # se saque for igual ou maior que 100 então
        nota_100 = nota_100 +1 # contador
        saque = saque - 100 # desconta valor de 100 no saque
    
    
    while saque >= 50:
        nota_50 = nota_50 +1
        saque = saque - 50

    while saque >= 20:
        nota_20 = nota_20 +1
        saque = saque - 20
    
    while saque >= 10:
        nota_10 = nota_10 +1
        saque = saque - 10

    while saque >= 1:
        nota_1 = nota_1 +1
        saque = saque - 1

# imprimindo na tela do user
print("Você vai receber \n %d notas de R$100 \n %d notas de R$50  \n %d notas de R$20  \n %d notas de R$10  \n %d notas de R$1 " %(nota_100, nota_50 , nota_20, nota_10, nota_1 ))





