import sys
import psycopg2

#colocar o caminho da pasta onde se localiza a conexão no sistema
sys.path.insert(0, 'C:/Users/Luism/OneDrive/Área de Trabalho/Workspace/consul-med-python/backend/database/')
sys.path.insert(1, 'C:/Users/Luism/OneDrive/Área de Trabalho/Workspace/consul-med-python/backend/model/')

from __connection__ import myConn
from __pessoa__ import Pessoa

connect = myConn()


def doInsertMedico(id_funcionario, crm):

    connect = myConn()
    sql = """INSERT INTO clinica.medico (id_funcionario, crm) VALUES (%s, %s) RETURNING medico.id_medico, medico.crm"""

    try:
        cur = connect.cursor()
        cur.execute(sql, (id_funcionario, crm,))
        
        connect.commit()
        for id_medico, crm in cur.fetchall() :
            print(id_medico, crm)
            return id_medico, crm

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()

def doSelectSingleMedico(id_medico):

    connect = myConn()
    sql = """SELECT * FROM clinica.medico WHERE id_medico = %s"""

    try:
        cur = connect.cursor()
        cur.execute(sql, (id_medico,))
        
        connect.commit()
        for id_medico, id_funcionario, crm in cur.fetchall() :
            print(id_medico, id_funcionario, crm)
            return id_medico, id_funcionario, crm

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()

def doSelectAllMedico():

    connect = myConn()
    sql = """SELECT * FROM clinica.medico"""

    try:
        cur = connect.cursor()
        cur.execute(sql)
        
        connect.commit()
        for id_medico, id_funcionario, crm in cur.fetchall() :
            print(id_medico, id_funcionario, crm)
            return id_medico, id_funcionario, crm

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()