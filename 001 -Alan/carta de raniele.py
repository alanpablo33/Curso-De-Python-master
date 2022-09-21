from tkinter import *

def carta():
    nome = input('Digite Seu Nome: ') # entrar com o nome senha

    if nome in ['Raniele','raniele','bombonzinho']: # si o nume estiver na lista então entre
        print("\nMuito Bem Você e o Amor da Minha Vida!")
        sim = input('\nDeseja abrir a carta virtual? ') # outra senha

        if sim in ['Sim','sim','s']: # se a sanha estiver na lista abra
            print("\nMuito Bem !")
            print('\n \n Minha Eterna Namorada! kkkkk '
              '\nEsse já e o nosso desimo dia dos namorados juntos meu amor,'
              '\ntemos fotos de todos ne, e gostos muito de tira-las por que '
              '\nvejo quem nos eramos a anos atras e vejo oque nos tornamos'
              '\nhoje, crescemos e evoluimos juntos vi você ficar cada dia'
              '\nmais linda e so me apaixonei cada dia mais por você.'
              '\nAgradeço a Deus todos os dia pela esposa linda que ele me'
              '\ndeu, uma que posso dizer que sim e minha parceira e que dou'
              '\nminha vida por ela sem pensar duas vezes, que esta contruindo'
              '\num ninho junto comigo, ta dificil mas logo vamos esta igual '
              '\ndois passarinhos la dentro da nossa casa e vamos poder'
              '\nfazer varios jantares juntos muito amor <3...'
              '\nEu te amo muito Raniele esse programa tem uma chave que só '
              '\nvocê pode abrir, igual o meu coração que só você e mais '
              '\nninguem nesse mundo pode ou consegue abrir linda.'
              '\nTe amo muito e quero viver toda a minha vida ao seu lado'
              '\ne ate depois dai junto a Deus. ')
            print('\n\n                               ASS: Alan Pablo Alves ')


        else:
            print("Que pena Você iria Gostar! ")

    else:
         print("Desculpe mas Você não e o meu bombonzinho!")


janela=Tk()
janela.title("Raniele")

texto_oriente = Label(janela, text= "Digite sua Senha para abrir a Carta")
texto_oriente.grid(column=0 , row=0) #linha e coluna

botao = Button(janela, text="Entrar" , command= carta)
botao.grid(column= 0 , row= 1)

tex_carta = Label(janela, text=" ")
tex_carta.grid(column= 0 , row= 2)

janela.mainloop()