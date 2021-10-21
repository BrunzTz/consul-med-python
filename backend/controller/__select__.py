import sys

#caminho para conexao
sys.path.insert(0, 'C:/Users/AULA/OneDrive/Área de Trabalho/consul-med-python/backend/model/')
sys.path.insert(1, 'C:/Users/AULA/OneDrive/Área de Trabalho/consul-med-python/backend/database/')

from __connection__ import myConn
from __pessoa__ import *

#Pessoa
doSelectAllPessoa()
doSelectSinglePessoa("27")

#Paciente


#Funcionario


#Medico