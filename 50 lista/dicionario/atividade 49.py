carro = {
    "pneus": 4,
    "portas": 2,
    "motor":1,
    "janelas": 4,
}

carro["Teto solar"]=1
print(carro)
del carro["motor"], carro["janelas"]
print(carro)