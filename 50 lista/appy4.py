notas= [10,5,8,3,7]
soma_notas = 0
i = 0

while i < 5:
    soma_notas = soma_notas + notas[i] #percorrendo a lista e somando valores 
    print("Notas das Provas: %d" %notas[i] )
    print("\n")
    i = i +1

media = soma_notas /5
print("Media: %.1f"% media)





