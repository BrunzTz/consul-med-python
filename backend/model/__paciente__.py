import sys
import psycopg2

#colocar o caminho da pasta onde se localiza a conexão no sistema
sys.path.insert(0, 'C:/Users/AULA/OneDrive/Área de Trabalho/consul-med-python/backend/database/')
sys.path.insert(1, 'C:/Users/AULA/OneDrive/Área de Trabalho/consul-med-python/backend/model/')

from __connection__ import myConn
from __pessoa__ import Pessoa

connect = myConn()


def doInsertPaciente(id_pessoa, peso, altura, pressao, tipo_sanguineo):

    connect = myConn()
    sql = """INSERT INTO clinica.paciente (id_pessoa, peso, altura, pressao, tipo_sanguineo) VALUES (%s, %s, %s, %s, %s) RETURNING paciente.id_paciente, paciente.peso, paciente.pressao"""

    try:
        cur = connect.cursor()
        cur.execute(sql, (id_pessoa, peso, altura, pressao, tipo_sanguineo,))
        
        connect.commit()
        for id_paciente, peso, pressao in cur.fetchall() :
            print(id_paciente, peso, pressao)
            return id_paciente, peso, pressao

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()

def doSelectSinglePaciente(id_paciente):

    connect = myConn()
    sql = """SELECT * FROM clinica.paciente WHERE id_paciente = %s"""

    try:
        cur = connect.cursor()
        cur.execute(sql, (id_paciente,))
        
        connect.commit()
        for id_paciente, id_pessoa, peso, altura, pressao, tipo_sanguineo in cur.fetchall() :
            print(id_paciente, id_pessoa, peso, altura, pressao, tipo_sanguineo)
            return id_paciente, id_pessoa, peso, altura, pressao, tipo_sanguineo

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()

def doSelectAllPaciente():

    connect = myConn()
    sql = """SELECT * FROM clinica.paciente"""

    try:
        cur = connect.cursor()
        cur.execute(sql)
        
        connect.commit()
        for id_paciente, id_pessoa, peso, altura, pressao, tipo_sanguineo in cur.fetchall() :
            print(id_paciente, id_pessoa, peso, altura, pressao, tipo_sanguineo)
            return id_paciente, id_pessoa, peso, altura, pressao, tipo_sanguineo

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()