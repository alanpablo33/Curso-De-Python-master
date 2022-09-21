#Repetições aninhadas

i = 0 #variavel 

while i <= 10: #primeiro loop
    print("i:%d" %i)

    x = 0 #variavel
    while x <= 5: # segundo loop dentro do primeiro loop
        print("x:%d" %x)
        x = x +1

    i = i +1

    # ficara o x dentro do i