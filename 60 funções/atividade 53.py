def par(l):
    lista = []

    for x in l:
        if x % 2 == 0:
            lista.append(x)
    return lista

lis=[1,2,3,4,5,6,7,8,9,10]


lis_par = par(lis)
print(lis_par)


        