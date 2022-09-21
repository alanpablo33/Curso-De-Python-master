# Buscando nome na lista

lista = ["Alan", "Pablo", "Alves" , "Silva"]

i = 0

nome_procurado = input("Qual nome você procura: ") # o que procura
achou = False


while i <len(lista): #tamanho da lista
    if lista[i] == nome_procurado: # se na lsita tiver nome == nome+
        print("Nome Encontrado %s!" %nome_procurado)
        achou = True  
    i = i +1

if achou == False:
    print("Nome Não encontrado %s" %nome_procurado)