def media(l): # função media
    lista=[]
    media= 0
    soma= 0

    for x in l:
        soma += x # ira somar os valores da lista
    media = soma / len(l) # ira dividir a soma pelo tamanho da lista dando assim a media
    return media
       

lis =[2,2,2]
lis.append(int(input("Digite os Valores: ")))
print(lis)

med= media(lis)

print("A media é: %d" %med)



