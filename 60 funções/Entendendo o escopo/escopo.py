from cgi import test


escopo_global = "Tchau" # pode ser usado em todo o codigo

def teste():
    teste = "Olá" # escopo local so pode ser usado dentro da função
    print(teste) 
    print(escopo_global)

teste()