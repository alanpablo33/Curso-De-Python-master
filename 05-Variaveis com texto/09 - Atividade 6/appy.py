x = True
y = False
z = False

print(x and y) # False
print(not x) # False
print(x and x) # True
print(y and y) # False
print(y or x) # True
print(y and z) # False
print(not y) # True
print(x and z) # False

# and : Só retornara True se todas forem verdadeiras
# or se uma for True, retornara True
# not inverte o valor se for False fica True, se for True fica False

nome= 'Alan Pablo'
idade= 2
carteira= True

print('Cidadao', nome, idade>18 and  carteira , 'Pode Dirigir')