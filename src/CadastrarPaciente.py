# Importar modulos 
from tkinter import *
from PIL import ImageTk
from tkcalendar import DateEntry # pip install tkcalendar

  
# Criar objeto
root = Tk()
  
# ajustar o tamanho  
root.geometry("1350x660+0+0")
root.resizable(0,0)
root.maxsize()
root.title("MedicSoft - Cadastrar Paciente")
root.iconbitmap("images/cadastrar.ico")


# Add imagem de fundo
bg = PhotoImage(file = "images/Paciente.png")
  
# Criando o Canvas
canvas1 = Canvas( root, width = 1350,
                 height = 600)
  
canvas1.pack(fill = "both", expand = True)
  
# imagem display
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

#Bem vindo
canvas1.create_text( 244, 35, text = "Cadastrar Paciente",
font=("Poppins SemiBold", 15), fill='white')

#Nome Completo
canvas1.create_text( 158, 125, text = "Nome Completo",
font=("Poppins Medium", 11), fill='#34444C')

entrynomec = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(445, 150, width = 702, height=25, window=entrynomec)
entrynomec.config(highlightbackground='#afeeee')


#Sexo
canvas1.create_text( 825, 125, text = "Sexo",
font=("Poppins Medium", 11), fill='#34444C')

entrysexo = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(827, 150, width = 40, height=25, window=entrysexo)
entrysexo.config(highlightbackground='#afeeee')

#Endereço
canvas1.create_text( 129, 185, text = "Endereço",
font=("Poppins Medium", 11), fill='#34444C')

entryendereco = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(345, 210, width = 502, height=25, window=entryendereco)

#Telefone
canvas1.create_text(635, 183, text = "Telefone",
font=("Poppins Medium", 11), fill='#34444C')

entryphone = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window( 728, 210, width=240, height= 25, window=entryphone)

#E-mail
canvas1.create_text(122, 245, text = "E-mail",
font=("Poppins Medium", 11), fill='#34444C')

entryemail = Entry (root, font=("Poppins Medium", 11), foreground='#308C83')
canvas1.create_window(280, 270, width = 370, height=25, window=entryemail)

#Data de Nascimento
canvas1.create_text(555, 245, text = "Data de Nascimento",
font=("Poppins Medium", 11), fill='#34444C')

cal = DateEntry(root, width=12, year=2001, month=4, day=27, 
background='#308c83', foreground='white', borderwidth=0)
cal.pack(padx=10, pady=10)
canvas1.create_window(557, 270, width = 157, height=25, window=cal)

#Peso
canvas1.create_text(690, 245, text = "Peso (kg)",
font=("Poppins Medium", 11), fill='#34444C')

entrypeso = Entry (root, font=("Poppins Medium", 11), foreground='#308C83')
canvas1.create_window(700, 270, width = 92, height=25, window=entrypeso)

#Altura
canvas1.create_text(810, 245, text = "Altura (m)",
font=("Poppins Medium", 11), fill='#34444C')

entryaltura = Entry (root, font=("Poppins Medium", 11), foreground='#308C83')
canvas1.create_window(815, 270, width = 92, height=25, window=entryaltura)


#CPF
canvas1.create_text(110, 310, text = "CPF",
font=("Poppins Medium", 11), fill='#34444C')

entrypeso = Entry (root, font=("Poppins Medium", 11), foreground='#308C83')
canvas1.create_window(200, 335, width = 211, height=25, window=entrypeso)

#Salvar
btnsalvar = Button(root, text="Salvar", font=("Poppins SemiBold", 11), width= 113, borderwidth=0, bg='#308c83', foreground ="#ffffff",
activebackground='#308c83', activeforeground='#ffffff')
canvas1.create_window(380, 335, width = 113, height=25, window=btnsalvar)

#fim
root.mainloop()