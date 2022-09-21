#Número primo é um numero que e 
# dividido apenas por ele mesmo e o numero 1

num = int(input("Digite um numero: ")) # entra com o valor

div = 0 

cont = num

while div > 0:

    if num % cont ==0: # divide o num por ele mesmo se for igual a 0 passa
        div = div +1
    num = num -1

# testando se o numero e primo
if div == 2:
    print("O numero %d é primo!" % num)
else:
    print("O numero %d NÃO e primo" % num)