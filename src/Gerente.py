# Importar modulos 
from tkinter import *
from PIL import ImageTk

  
# Criar objeto
root = Tk()
  
# ajustar o tamanho  
root.geometry("1350x660+0+0")
root.resizable(0,0)
root.maxsize()
root.title("MedicSoft - Gerencia")
root.iconbitmap("images/network.ico")


# Add imagem de fundo
bg = PhotoImage(file = "images/Gerente.png")
  
# Criando o Canvas
canvas1 = Canvas( root, width = 1350,
                 height = 600)
  
canvas1.pack(fill = "both", expand = True)
  
# imagem display
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

#Bem vindo
canvas1.create_text( 244, 35, text = "Bem vindo ao nosso sistema!",
font=("Poppins SemiBold", 15), fill='white')

#Botao Gerar relatórios
btnrelatorios = Button(root, text="Gerar relatórios", font=("Poppins Medium", 11), width= 113,
borderwidth=0, bg='#308c83', foreground ="#ffffff",
activebackground='#308c83', activeforeground='#ffffff')
canvas1.create_window(185, 133, width = 185, height=26, window=btnrelatorios)

#Botao Funcionário
btnfuncionario = Button(root, text="Funcionários", font=("Poppins Medium", 11), width= 113,
borderwidth=0, bg='#308c83', foreground ="#ffffff",
activebackground='#308c83', activeforeground='#ffffff')
canvas1.create_window(185, 175, width = 185, height=26, window=btnfuncionario)


#fim
root.mainloop()