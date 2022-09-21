teste ="Palavra"
nome = "Alan Pablo Alves "
# ira pegar os caracter 0 e 1 e parar no 2, o dois ele não vai buscar
print(teste[0:2])
# pode manipular da maneira que quiser 
print(nome[2:6])

frase ="Hoje esta fazendo sol aqui em diamantina"
# busquei somenta a palavra sol que esta entre o 18:21
print(frase[18:21])
# 18:21 e a palavra sol
#criei uma variavel sol para o valor 18:21
sol = frase[18:21]
# chamei o sol
print(sol)
# fiz numa nova frase com a variavel sol
print("Temos um dia de %s hoje" %sol)

print("\n")

s= "Abacate"
# vai comecar do 0 ate o 3
print(s[:3])

# Vai comecar do 3 e vai seguir
print(s[3:])

# vai ler ate o 3
print(s[0:-3])