#acahar menor valor

lista = [1,2,3,4,5,6,7,8,9]

menor_numero =10 #variavel menor

for n in lista: # n elemento na lista
    if n < menor_numero: # se n for maior que menor numero 
        menor_numero = n # menor numero e n
print("O Menor numero e o %d" %menor_numero)