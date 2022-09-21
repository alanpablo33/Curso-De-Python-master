dicionario= {
    "Idade" : 25,
    "Nome": "Alan",
    "Veiculo": "Moto"
}

print(dicionario) #imprimindo dicionario

print("Nome" in dicionario) # verificando se existe esse valor no dicionario
print("Sobrenome" in dicionario)# verificndo em dicionario

if "Nome" in dicionario:
    print(" O seu nome é %s" % dicionario["Nome"]) # resultado 
if "Sobrenome" in dicionario:
    print("O seu sobrenome é %s" % dicionario["Sobrenome"])

