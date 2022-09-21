#Estrutura de repetição while

numero= int(input("Digite o numero de vezes: "))
print(numero)

print("Antes do Loop")

while numero <5: # enquanto a VARIAVEL numero for menor que 5 repita
    print(numero) # mostrte a contagem
    numero = numero +1 # add +1 a numero

    if numero == 3:
        print("O Numero e 3!") # pode se usar if dentro do while
        

print("Depois do loop") # indicação de termino