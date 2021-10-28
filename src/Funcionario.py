# Importar modulos 
from tkinter import *
from PIL import ImageTk
from tkcalendar import DateEntry # pip install tkcalendar

#Salvar
def salvar():
    print("Nome",entrynome.get())
    print("Endereco",entryendereco.get())
    print("Telefone",entrytelefone.get())
    print("CPF",entrycpf.get())
    print("Sexo",entrysexo.get())
    print("Data Nascimento",dataNasc.get())
    print("Email",entryemail.get())
    print("Salario",entrysalario.get())
    print("Atribuicao",clicked.get())
  
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
canvas1.create_text( 244, 35, text = "Cadastrar Funcionário",
font=("Poppins SemiBold", 15), fill='white')

#Nome
canvas1.create_text( 115, 125, text = "Nome",
font=("Poppins Medium", 11), fill='#34444C')

entrynome = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(445, 150, width = 702, height=25, window=entrynome)
entrynome.config(highlightbackground='#afeeee')

#Endereço
canvas1.create_text( 125, 185, text = "Endereco",
font=("Poppins Medium", 11), fill='#34444C')

entryendereco = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(330, 210, width = 472, height=25, window=entryendereco)
entryendereco.config(highlightbackground='#afeeee')

#Telefone
canvas1.create_text( 625, 185, text = "Telefone",
font=("Poppins Medium", 11), fill='#34444C')

entrytelefone = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(695, 210, width = 200, height=25, window=entrytelefone)
entrytelefone.config(highlightbackground='#afeeee')

#CPF
canvas1.create_text( 108, 245, text = "CPF",
font=("Poppins Medium", 11), fill='#34444C')

entrycpf = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(245, 270, width = 300, height=25, window=entrycpf)
entrycpf.config(highlightbackground='#afeeee')

#Sexo
canvas1.create_text( 440, 245, text = "Sexo",
font=("Poppins Medium", 11), fill='#34444C')

entrysexo = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(445, 270, width = 40, height=25, window=entrysexo)
entrysexo.config(highlightbackground='#afeeee')

#Data Nascimento
canvas1.create_text(560, 245, text = "Data Nascimento",
font=("Poppins Medium", 11), fill='#34444C')

dataNasc = DateEntry(root, width=12, year=2021, month=10, day=17, 
background='#308c83', foreground='white', borderwidth=0)
dataNasc.pack(padx=10, pady=10)
canvas1.create_window(610, 270, width = 211, height=25, window=dataNasc)

#Email
canvas1.create_text( 111, 305, text = "Email",
font=("Poppins Medium", 11), fill='#34444C')

entryemail = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(405, 330, width = 625, height=25, window=entryemail)
entryemail.config(highlightbackground='#afeeee')

#Salário
canvas1.create_text( 115, 365, text = "Salário",
font=("Poppins Medium", 11), fill='#34444C')

entrysalario = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(220, 390, width = 255, height=25, window=entrysalario)
entrysalario.config(highlightbackground='#afeeee')

#Atribuição
""" canvas1.create_text( 425, 365, text = "Atribuição",
font=("Poppins Medium", 11), fill='#34444C')

entryatribuicao = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
canvas1.create_window(545, 390, width = 305, height=25, window=entryatribuicao)
entryatribuicao.config(highlightbackground='#afeeee') """

def option_changed(self, *args):
    print("Atribuicao", self)
    if (self == 'Medico'):
        #CRM
        canvas1.create_text( 110, 425, text = "CRM",
        font=("Poppins Medium", 11), fill='#34444C')

        entrycrm = Entry (root, font=("Poppins Medium", 11), foreground='#308C83') 
        canvas1.create_window(220, 450, width = 255, height=25, window=entrycrm)
        entrycrm.config(highlightbackground='#afeeee')

canvas1.create_text( 425, 365, text = "Atribuição",
font=("Poppins Medium", 11), fill='#34444C')

options = [ 
    "Atendente",
    "Medico",
    "Gerente"
]

clicked = StringVar()
clicked.set(options[0])

atribuicao = OptionMenu(root, clicked, *options, command=option_changed)
atribuicao.pack(pady=20)
atribuicao.config(font=("Poppins SemiBold", 12), bg='#ffffff', foreground ="#308C83", activebackground='#FFFFFF', activeforeground='#c2f2ed',
border=0)

canvas1.create_window(545, 390, width = 305, height=25, window=atribuicao)

#Salvar
btnsalvar = Button(root, text="Salvar", width= 113, borderwidth=0, bg='#308c83', foreground ="#ffffff",
activebackground='#308c83', activeforeground='#ffffff', command=salvar)
canvas1.create_window(451, 450, width = 113, height=25, window=btnsalvar)

"""
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
canvas1.create_window(529, 270, width = 113, height=25, window=btnsalvar) """

#fim
root.mainloop()