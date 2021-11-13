import sys

#caminho para conexao
sys.path.insert(0, 'C:/Users/Luism/OneDrive/Área de Trabalho/Workspace/consul-med-python/backend/model/')
sys.path.insert(1, 'C:/Users/Luism/OneDrive/Área de Trabalho/Workspace/consul-med-python/backend/database')

from __connection__ import myConn
from __pessoa__ import *
from __atribuicao__ import *
from __medico__ import *
from __paciente__ import *
from __funcionario__ import *

#Pessoa
doSelectAllPessoa()
doSelectSinglePessoa("27")

#Paciente
doSelectSinglePaciente(1)
doSelectAllPaciente()

#Funcionario
doSelectSingleFuncionario(2)
doSelectAllFuncionario()

#Medico
doSelectAllMedico()
doSelectSingleMedico(1)

#Atribuicao
doSelectAllAtribuicao()
doSelectSingleAtribuicao(1)