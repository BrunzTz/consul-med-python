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
root.title("MedicSoft - Cadastrar Consulta")
root.iconbitmap("images/network.ico")


# Add imagem de fundo
bg = PhotoImage(file = "images/AtendenteCadastrarConsulta.png")
  
# Criando o Canvas
canvas1 = Canvas( root, width = 1350,
                 height = 600)
  
canvas1.pack(fill = "both", expand = True)
  
# imagem display
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

#Bem vindo
canvas1.create_text( 244, 35, text = "Cadastrar Consulta",
font=("Poppins SemiBold", 15), fill='white')

#Paciente
canvas1.create_text( 128, 125, text = "Paciente",
font=("Poppins Medium", 11), fill='#34444C')

entrypaciente = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(445, 150, width = 702, height=25, window=entrypaciente)
entrypaciente.config(highlightbackground='#afeeee')

#Médico
canvas1.create_text( 122, 185, text = "Médico",
font=("Poppins Medium", 11), fill='#34444C')

entrypaciente = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(345, 210, width = 502, height=25, window=entrypaciente)

#Status
canvas1.create_text(635, 183, text = "Status",
font=("Poppins Medium", 11), fill='#34444C')

options = [ 
"Disponível",
"Ocupado",
"Ausente"
]

clicked = StringVar()
clicked.set(options[0])

status = OptionMenu(root, clicked, *options)
status.pack(pady=20)
status.config(font=("Poppins SemiBold", 12), bg='#ffffff', foreground ="#308C83", activebackground='#FFFFFF', activeforeground='#c2f2ed',
border=0)

canvas1.create_window( 700, 210, width=188, height= 25, window=status)

#Data
canvas1.create_text(115, 245, text = "Data",
font=("Poppins Medium", 11), fill='#34444C')

cal = DateEntry(root, width=12, year=2021, month=10, day=17, 
background='#308c83', foreground='white', borderwidth=0)
cal.pack(padx=10, pady=10)
canvas1.create_window(175, 270, width = 161, height=25, window=cal)

#Horario
canvas1.create_text(309, 245, text = "Horário",
font=("Poppins Medium", 11), fill='#34444C')

entryhorario = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(360, 270, width = 158, height=25, window=entryhorario)

#Salvar
btnsalvar = Button(root, text="Salvar", width= 113, borderwidth=0, bg='#308c83', foreground ="#ffffff",
activebackground='#308c83', activeforeground='#ffffff')
canvas1.create_window(529, 270, width = 113, height=25, window=btnsalvar)

#fim
root.mainloop()