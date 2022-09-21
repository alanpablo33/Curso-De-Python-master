from unicodedata import name


nome= input("Digite seu nome: ")
idade= int(input("Digite sua idade: "))

if idade >= 18:
    print( "Ola Sr.%s" %nome + " Fique a Vontade" )

else:
    print("Você não tem idade pra isso")
