def checa_tamanho_texto(texto):
    ress = ""

    if len(texto) >=20:
        ress= "Texto e longo!"
    else:
        ress= "Texto e curto!"
    return ress

        
text1= input("Digite um texto: ")

tex = checa_tamanho_texto(text1)

print(tex)
print(len(text1))