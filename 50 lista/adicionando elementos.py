# função append(valor)

lista = [0,1,2,3,4]
#para adicionar um novo valor a lista usa-se o append ex: lista.append(valor que deseja add)
lista.append(3000)
print(lista)

nome= ["Alan", "Alves"]
nome.append(input("Digite o novo nome a Lista:  "))
print("Após input")
print(nome)

if nome[2] != "Maria":
    nome.append("Maria")

print("Após if")
print(nome)

