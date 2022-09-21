def nomee(a):
    a= input("Digite seu nome: ")
    return a

def idadee(b):
    b= int(input("Digite sua idade:"))
    return b

def profisssaoo(c):
    c= input("Digite sua Profissão: ")
    return c

def perfil(a,b,c,f):
    resultado = f(a,b,c)
    return resultado


t=perfil(nomee(""),idadee(""),profisssaoo(""))
print(t)
