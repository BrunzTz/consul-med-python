# Importar modulos 
from tkinter import *
from PIL import ImageTk

  
# Criar objeto
root = Tk()
  
# ajustar o tamanho  
root.geometry("1350x660+0+0")
root.resizable(0,0)
root.maxsize()
root.title("MedicSoft - Bem vindo, atendente!")
root.iconbitmap("images/network.ico")


# Add imagem de fundo
bg = PhotoImage(file = "images/Atendente.png")
  
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

#Bem vindo
canvas1.create_text( 144, 110, text = "Cadastrar",
font=("Poppins Regular", 15), fill='#34444c')

#combo_box cadastrar
options = [ "Paciente","Consulta"]

clicked = StringVar()
clicked.set(options[0])

cadastrar = OptionMenu(root, clicked, *options)
cadastrar.pack(pady=20)
cadastrar.config(font=("Poppins SemiBold", 12), bg='#308C83', foreground ="#ffffff", activebackground='#308C83', activeforeground='#c2f2ed',
border=0)

canvas1.create_window( 182, 138, width=178, height= 30, window=cadastrar)

#Botao ok
btnok = Button(root, text="Ok", width= 113, borderwidth=0, bg='#308c83', foreground ="#ffffff",
activebackground='#308c83', activeforeground='#ffffff')
canvas1.create_window(335, 138, width = 113, height=26, window=btnok)


#fim
root.mainloop()