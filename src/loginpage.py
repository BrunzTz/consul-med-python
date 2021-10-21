# Importar modulos 
from tkinter import *
from PIL import ImageTk
  
# Criar objeto
root = Tk()
  
# ajustar o tamanho  
root.geometry("1350x660+0+0")
root.resizable(0,0)
root.maxsize()
root.title("Fazer Login")
root.iconbitmap("images/network.ico")

# Add imagem de fundo
bg = PhotoImage(file = "images/loginscreen.png")
  
# Criando o Canvas
canvas1 = Canvas( root, width = 1350,
                 height = 600)
  
canvas1.pack(fill = "both", expand = True)
  
# imagem display
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

#Comando Sair
def Sair():
    exit()

# Inputs
entryemail = Entry (root, borderwidth=0, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(680, 220, width = 480, window=entryemail)

entrysenha = Entry (root,text="Placeholder text", show="*", borderwidth=0,
font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(680, 325, width = 480, window=entrysenha)

#botoe
btnlogin = Button(root, text="Login", width= 38, borderwidth=0, bg='#308C83', foreground ="#fafafa",
activebackground='#308c83', activeforeground='#ffffff')
canvas1.create_window(544, 414, width = 200, window=btnlogin)

btnsair = Button(root, text="Sair", width= 38, borderwidth=0, bg='#ffffff', foreground ="#308c83",
activebackground='#ffffff', activeforeground='#308c83', command=Sair)
canvas1.create_window(812, 414, width = 200, window=btnsair)


#fim
root.mainloop()
