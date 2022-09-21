lista = ["Alan", "Pedor" , "Alves"]

i = 0

busca = input("Digite o que busca: ")
busca2 = input("Digite o segundo: ")

while i < len(lista):
    if lista[i] == busca:
        print("Isso ai %s" %busca)
        
    elif lista[i] == busca2:
        print("Segundo %s" %busca2)
    
    i = i + 1