# Percorre toda a lista e deleta os elementos que estiverem no indice 4

#lista=[1,2,3,4,5,6,7,8,9,10]

#i = 0

#while i < len(lista):
#    del lista[4]
#    i = i +1
#    print(lista)

#percorre a lista e deleta o valor 4

lista2=[]

i=0

while i <=10: #criando lista de forma dinamica
    lista2.append(i)
    i = i + 1

print(lista2)

j = 0

while j < len(lista2): # percorrendo lista 
    if lista2[j] == 4: # quando o elemento for == 4 delete
        del lista2[j]
    j = j + 1
print(lista2)