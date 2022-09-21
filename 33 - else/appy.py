poupanca= int(input("Digite o valor da Poupança: "))
saque= int(input("Digite o valor do Seu Saque: "))

print("Poupança: %d" %poupanca)
print("Saque: %d" %saque)

if (saque <= poupanca):
    print("Você sacou R$%d" %saque)
    poupanca= poupanca - saque
    print("Ainda na Poupança: R$%d" %poupanca)
else:
    print("Você não tem saldo para sacar R$%d" %saque)
    print("Sua poupança tem no momento R$%d" %poupanca)