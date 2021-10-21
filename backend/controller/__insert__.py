import sys

#caminho para conexao
sys.path.insert(0, 'C:/Users/AULA/OneDrive/Área de Trabalho/consul-med-python/backend/model/')
sys.path.insert(1, 'C:/Users/AULA/OneDrive/Área de Trabalho/consul-med-python/backend/database/')

from __connection__ import myConn
from __pessoa__ import *
from __paciente__ import *
from __funcionario__ import *
from __medico__ import *
from __atribuicao__ import *

#Inserir Paciente
def insertPaciente(nome, endereco, telefone, cpf, sexo, data_nasc, email, peso, altura, pressao, tipo_sang):

    pessoa = Pessoa(nome, endereco, telefone, cpf, sexo, data_nasc, email)

    def id_pessoa(pessoa):
        id = doInsertPessoa(pessoa.getNome(), pessoa.getEndereco(), pessoa.getTelefone(), pessoa.getCPF(), pessoa.getSexo(), pessoa.getData_nasc(), pessoa.getEmail())
        return id

    id = id_pessoa(pessoa)

    def insertPaciente(id_pessoa, peso, altura, pressao, tipo_sang):
        paciente = doInsertPaciente(id_pessoa, peso, altura, pressao, tipo_sang)

    insertPaciente(id, peso, altura, pressao, tipo_sang)

#Inserir Atribuição
def insertAtribuicao(tipo):

    id = doInsertAtribuicao(tipo)
    return id
    
#Inserir Funcionário
def insertFuncionario(nome, endereco, telefone, cpf, sexo, data_nasc, email, supervisor, salario, tipo_atribuicao):

    pessoa = Pessoa(nome, endereco, telefone, cpf, sexo, data_nasc, email)

    def id_pessoa(pessoa):
        id = doInsertPessoa(pessoa.getNome(), pessoa.getEndereco(), pessoa.getTelefone(), pessoa.getCPF(), pessoa.getSexo(), pessoa.getData_nasc(), pessoa.getEmail())
        return id

    idPessoa = id_pessoa(pessoa)

    idAtribuicao = doSelectSingleAtribuicao(tipo_atribuicao)

    doinsertFuncionario(idPessoa, idAtribuicao, salario, supervisor)

    return




pessoa = Pessoa("Luis", "Rua tal", "1234", "1234", "M", "2021-01-01", "luuis@email.com")

id_pessoa = doInsertPessoa(pessoa.getNome(), pessoa.getEndereco(), pessoa.getTelefone(), pessoa.getCPF(), pessoa.getSexo(), pessoa.getData_nasc(), pessoa.getEmail())
print(id_pessoa)