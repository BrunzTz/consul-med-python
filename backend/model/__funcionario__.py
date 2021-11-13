import sys
import psycopg2

#colocar o caminho da pasta onde se localiza a conexão no sistema
sys.path.insert(0, 'C:/Users/Luism/OneDrive/Área de Trabalho/Workspace/consul-med-python/backend/database/')
sys.path.insert(1, 'C:/Users/Luism/OneDrive/Área de Trabalho/Workspace/consul-med-python/backend/model/')

from __connection__ import myConn
from __pessoa__ import Pessoa

connect = myConn()

def doinsertFuncionario(idPessoa, idAtribuicao, salario, supervisor):

    connect = myConn()
    sql = """INSERT INTO clinica.funcionario (id_pessoa, id_atribuicao, salario, supervisor) VALUES (%s, %s, %s, %s) RETURNING funcionario.id_funcionario, funcionario.salario"""

    try:
        cur = connect.cursor()
        cur.execute(sql, (idPessoa, idAtribuicao, salario, supervisor,))
        
        connect.commit()
        for id_funcionario, salario in cur.fetchall() :
            print(id_funcionario, salario)
            return id_funcionario

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()

def doSelectSingleFuncionario(id_funcionario):

    connect = myConn()
    sql = """SELECT * FROM clinica.funcionario WHERE id_funcionario = %s"""

    try:
        cur = connect.cursor()
        cur.execute(sql, (id_funcionario,))
        
        connect.commit()
        for id_funcionario, id_pessoa, id_atribuicao, salario, supervisor in cur.fetchall() :
            print(id_funcionario, id_pessoa, id_atribuicao, salario, supervisor)
            return id_funcionario, id_pessoa, id_atribuicao, salario, supervisor

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()

def doSelectAllFuncionario():

    connect = myConn()
    sql = """SELECT * FROM clinica.funcionario"""

    try:
        cur = connect.cursor()
        cur.execute(sql)
        
        connect.commit()
        for id_funcionario, id_pessoa, id_atribuicao, salario, supervisor in cur.fetchall() :
            print(id_funcionario, id_pessoa, id_atribuicao, salario, supervisor)
            return id_funcionario, id_pessoa, id_atribuicao, salario, supervisor

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()