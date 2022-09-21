produto1 =["Camisa" , "Azul", 50.50]
produto2 =["Calça", "Jeans", 70.59]
produto3 =["Boné", "Vermelho", 200.87]

lista= [produto1,produto2,produto3]
print(lista)

for x in lista:
    print("Produto: %s" %x[0] ,"Cor: %s" %x[1] , "Preço: %.2f" %x[2])