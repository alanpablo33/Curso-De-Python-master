#declarando variavel
numero_texto = input("Digite um numero: ")
print(numero_texto)

#para que isso seja possivel a primeira variavel tem que ser um int e a segunda tbm
#Por isso fazemos a converção de variaveis

numero = int(numero_texto) #conversão
novo_numero = 5 + numero #soma
print(novo_numero)

# tbm pode ser feito de uma forma mais direta assim 
novo_numero = int(input("Digite mais um numero: "))
print(numero + novo_numero)

# da mesma forma funciona com o float
novo_float = float(input("Digite o que você tem de dinheiro na carteira: "))
print(novo_float)
soma_float = 100.48 + novo_float

print(soma_float)