def soma(a,b): # função soma
    return a + b

def multiplicacao(a,b): # função multiplicação
    return a * b

def operacao(a,b , f): # função operação 
    resultado = f(a,b) # a variavel f ira chamar a função que deseja executar para resolver o problema
    return resultado

a = operacao(5,5, soma) # f chamou soma para resolver a e b
print(a)

b = operacao(5,5, multiplicacao) # opercao chamou multiplicação para resolver a e b
print(b)