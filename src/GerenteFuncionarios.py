# Importar modulos 
from tkinter import *
from PIL import ImageTk
from tkinter import ttk

  
# Criar objeto
root = Tk()
  
# ajustar o tamanho  
root.geometry("1350x660+0+0")
root.resizable(0,0)
root.maxsize()
root.title("MedicSoft - Funcionários")


# Add imagem de fundo
bg = PhotoImage(file = "images/Gerente-Funcionarios.png")
  
# Criando o Canvas
canvas1 = Canvas( root, width = 1350,
                 height = 600)
  
canvas1.pack(fill = "both", expand = True)
  
# imagem display
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

#Label
canvas1.create_text( 244, 35, text = "Funcionários",
font=("Poppins SemiBold", 15), fill='white')

#Label2
canvas1.create_text( 285, 115, text = "Listagem de Funcionários",
font=("Poppins SemiBold", 13), fill='black')

#Botao Cadastrar
btnCadastrar = Button(root, text="Cadastrar", font=("Poppins SemiBold", 12), width= 113,
borderwidth=0, bg='#308c83', foreground ="#ffffff",
activebackground='#64D8CC', activeforeground='#308c83')
canvas1.create_window(1019, 115, width = 155, height=33, window=btnCadastrar)

#Botao Atualizar
btnAtualizar = Button(root, text="Atualizar", font=("Poppins SemiBold", 12), width= 113,
borderwidth=0, bg='#F2D055', foreground ="#ffffff",
activebackground='#FCE38D', activeforeground='#F2D055')
canvas1.create_window(1019, 230, width = 155, height=33, window=btnAtualizar)

#Botao Deletar
btnDeletar = Button(root, text="Deletar", font=("Poppins SemiBold", 12), width= 113,
borderwidth=0, bg='#F25555', foreground ="#ffffff",
activebackground='#FFA8A8', activeforeground='#F25555')
canvas1.create_window(1019, 275, width = 155, height=33, window=btnDeletar)

#Lista de Funcionários // NAO ESTÁ CERTO!!!
listaNomes=[['0','Yasmin','9875'],['1','Luis','2341'],['3','Bruno','3784']]

tv=ttk.Treeview(root,columns=('id','nome','fone'), show='headings')
tv.column('id',minwidth=0, width=50)
tv.column('nome',minwidth=0, width=250)
tv.column('fone',minwidth=0, width=100)
tv.heading('id', text='ID')
tv.heading('nome', text='Nome')
tv.heading('fone', text='Telefone')
tv.pack()
canvas1.create_window((500, 280), width= 450, height= 200, window=tv)


#fim
root.mainloop()
