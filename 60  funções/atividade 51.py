a = 20
b= 10
c = 3

def numero(num):
  

    ress = ""

    if num > 10:
       ress= "Numero e +"

    elif num < 10:
      ress=  "Numero e -"

    else:
        ress = "Igual a 10"

    return ress # retorno 

res_um = numero(a)
print(res_um)