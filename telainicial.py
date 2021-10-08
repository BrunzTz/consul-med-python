# Importar modulos 
from tkinter import *
from PIL import ImageTk
  
# Criar objeto
root = Tk()
  
# ajustar o tamanho  
root.geometry("1350x660+0+0")
root.resizable(0,0)
root.maxsize()
root.title("MedicSoft - Inicial")
root.iconbitmap("images/network.ico")

# Add imagem de fundo
bg = PhotoImage(file = "images/Principal.png")
  
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

#botão Home
btnhome = Button(root, text= "Inicio", width = 105, borderwidth = 0, bg='#ffffff', foreground= "#308c83",
activebackground='#C2F2ED', activeforeground='#308C83', font=("Poppins SemiBold", 10))
canvas1.create_window(50, 100, width = 111, height = 20, window=btnhome)

#botão Diagnosticos

#botão Consultas

#botão Sair
btnsair = Button(root, text= "Sair", width = 105, borderwidth = 0, bg='#ffffff', foreground= "#308c83",
activebackground='#C2F2ED', activeforeground='#308C83', font=("Poppins SemiBold", 10), command=Sair)
canvas1.create_window(50, 369, width = 111, height = 20, window=btnsair)

#botão Paciente
btnpaciente = Button(root, text="Paciente", width= 132, borderwidth=0, bg='#c2f2ed', foreground ="#308c83",
activebackground='#C2F2ED', activeforeground='#308C83', font=("Poppins SemiBold", 8))
canvas1.create_window(522, 273, width = 75, height = 20, window=btnpaciente)
# 522, 227

#NAO FINALIZADO!!!
#fim
root.mainloop()
