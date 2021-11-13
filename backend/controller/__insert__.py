import sys

#caminho para conexao
sys.path.insert(0, 'C:/Users/Luism/OneDrive/Área de Trabalho/Workspace/consul-med-python/backend/model/')
sys.path.insert(1, 'C:/Users/Luism/OneDrive/Área de Trabalho/Workspace/consul-med-python/backend/database/')

from __connection__ import myConn
from __pessoa__ import *
from __paciente__ import *
from __funcionario__ import *
from __medico__ import *
from __atribuicao__ import *

#Inserir Paciente
def insertPaciente(nome, endereco, telefone, cpf, sexo, data_nasc, email, peso, altura, pressao, tipo_sanguineo):

    pessoa = Pessoa(nome, endereco, telefone, cpf, sexo, data_nasc, email)

    def id_pessoa(pessoa):
        id = doInsertPessoa(pessoa.getNome(), pessoa.getEndereco(), pessoa.getTelefone(), pessoa.getCPF(), pessoa.getSexo(), pessoa.getData_nasc(), pessoa.getEmail())
        return id

    id = id_pessoa(pessoa)

    def insertPaciente(id_pessoa, peso, altura, pressao, tipo_sanguineo):
        paciente = doInsertPaciente(id_pessoa, peso, altura, pressao, tipo_sanguineo)
        return paciente

    insertPaciente(id, peso, altura, pressao, tipo_sanguineo)

#Inserir Atribuição
def insertAtribuicao(tipo):

    id = doInsertAtribuicao(tipo)
    return id
    
#Inserir Funcionário
def insertFuncionario(nome, endereco, telefone, cpf, sexo, data_nasc, email, supervisor, salario, id_atribuicao):

    pessoa = Pessoa(nome, endereco, telefone, cpf, sexo, data_nasc, email)

    def id_pessoa(pessoa):
        id = doInsertPessoa(pessoa.getNome(), pessoa.getEndereco(), pessoa.getTelefone(), pessoa.getCPF(), pessoa.getSexo(), pessoa.getData_nasc(), pessoa.getEmail())
        return id

    idPessoa = id_pessoa(pessoa)

    idAtribuicao = doSelectSingleAtribuicao(id_atribuicao)

    func = doinsertFuncionario(idPessoa, idAtribuicao, salario, supervisor)

    return func

#Inserir médico
def insertMedico(nome, endereco, telefone, cpf, sexo, data_nasc, email, supervisor, salario, id_atribuicao, crm):

    funcionario = insertFuncionario(nome, endereco, telefone, cpf, sexo, data_nasc, email, supervisor, salario, id_atribuicao)

    medico = doInsertMedico(funcionario, crm)

    return medico

#print(insertMedico("Yasmin", "Fim do mundo", "1234", "1234", "F", "2001-01-01", "Yasmin@email.com", "TRUE", 2134, 2, "2349876"))
#print(insertFuncionario("Yasmin", "Fim do mundo", "1234", "1234", "F", "2001-01-01", "Yasmin@email.com", "TRUE", 2134, 2))
#print(insertPaciente("Luis Henrique Macedo", "Rua teste", "1234", "33454556", "M", "2021-01-01", "Luis@emailteste.com", 91, 1.9, "100", "O+"))
#print(insertAtribuicao("Atendente"))