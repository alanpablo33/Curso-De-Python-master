#break

num = int(input("Digite um numero: "))

while num <= 10:
    print(num)
    if num == 5: # se num for igual a 5 então exit
        break 
    num = num +1
