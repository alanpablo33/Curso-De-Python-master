#Copia de Lista p2

#para add um valor a nova lista sem alterar a primeira lista usamos a [:] ex.

lista = ["Alan" , "Fernando", "Pedro"]

nova_lista = lista[:] #sintaxe

print(lista)
print(nova_lista)

nova_lista[0]= "João" #alteração sendo feita
print("\n\nAlteração na Lista: ")
print(lista) #primeira lista
print(nova_lista) #segunda lista