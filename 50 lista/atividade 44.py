lista = [ 1,2,3,4,5,6,7,8,9]

n = int(input("Digite o Numero: "))

encontrado = False

for o in lista: #buscando numero com for
    if n == o :
        print("O numero que você procura e o %d" %n)
        encontrado = True

if encontrado == False:
    print("Não encontramos o número %d" %n)

