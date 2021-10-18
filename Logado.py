# Importar modulos 
from tkinter import *
from PIL import ImageTk
  
# Criar objeto
root = Tk()
  
# ajustar o tamanho  
root.geometry("1350x660+0+0")
root.resizable(0,0)
root.maxsize()
root.title("MedicSoft - Bem vindo!!")
root.iconbitmap("images/network.ico")

# Add imagem de fundo
bg = PhotoImage(file = "images/bemvindo.png")
  
# Criando o Canvas
canvas1 = Canvas( root, width = 1350,
                 height = 600)
  
canvas1.pack(fill = "both", expand = True)
  
# imagem display
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

#Bem vindo
canvas1.create_text( 686, 383, text = "Bem vindo ao medicSoft, deseja entrar como?",
font=("Poppins SemiBold", 15), fill='white')

#botão Atendente
btnAtendente = Button(root, text="ATENDENTE", width= 194, borderwidth=0, bg='#308C83', foreground ="#ffffff",
activebackground='#308C83', activeforeground='#c2f2ed', font=("Poppins SemiBold", 15))
canvas1.create_window(477, 455, width = 150, height = 30, window=btnAtendente)

#botão Médico
btnMedico = Button(root, text="MÉDICO", width= 194, borderwidth=0, bg='#308C83', foreground ="#ffffff",
activebackground='#308C83', activeforeground='#c2f2ed', font=("Poppins SemiBold", 15))
canvas1.create_window(697, 455, width = 150, height = 30, window=btnMedico)

#botão Gerente
btnGerente = Button(root, text="GERENTE", width= 194, borderwidth=0, bg='#308c83', foreground ="#ffffff",
activebackground='#308C83', activeforeground='#c2f2ed', font=("Poppins SemiBold", 15))
canvas1.create_window(920, 455, width = 150, height = 30, window=btnGerente)


#fim
root.mainloop()