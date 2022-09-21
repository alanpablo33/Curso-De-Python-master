def saudacao(nome): # criando função olá nome
    return "Olá %s" %nome # retorno

sds = saudacao("Alan")  # inserindo a função a uma variavel

print(sds + ", Tudo bem?") # concatenando variavel que recebeu a função com um texto 

def soma(a, b): # criando função soma
    return a + b # retorno

s = soma(10 , 5) # dando valores e inserindo a uma variavel
d = soma(10, 6)

print(s) # chamando a variavel com o valor 

print(s + 5)

print(s + d)

def profissao(nome): # função profição
    p = " " # variavel a receber valor
    if nome == "Alan":
        p = "Programador"
    else:
        p="Não indentificado"
    return p # retorno 

prof = profissao("João")
print(prof)

prof1 = profissao("Alan")
print(prof1)