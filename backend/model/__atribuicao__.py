import sys
import psycopg2

#colocar o caminho da pasta onde se localiza a conexão no sistema
sys.path.insert(0, 'C:/Users/Luism/OneDrive/Área de Trabalho/Workspace/consul-med-python/backend/database/')

from __connection__ import myConn

connect = myConn()

def doInsertAtribuicao(tipo):

    connect = myConn()
    sql = """INSERT INTO clinica.atribuicao (tipo) VALUES (%s) RETURNING atribuicao.tipo, atribuicao.id_atribuicao"""

    try:
        cur = connect.cursor()
        cur.execute(sql, (tipo,))
        
        connect.commit()
        for tipo in cur.fetchall() :
            print(tipo)
            return tipo

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()

def doSelectAllAtribuicao():

    connect = myConn()
    sql = """SELECT id_atribuicao, tipo FROM clinica.atribuicao"""

    try:
        cur = connect.cursor()
        cur.execute(sql)
        
        connect.commit()

        for id_atribuicao, tipo in cur.fetchall() :
            print(id_atribuicao, tipo)
            return (id_atribuicao, tipo)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()

def doSelectSingleAtribuicao(id):

    connect = myConn()
    sql = """SELECT id_atribuicao FROM clinica.atribuicao WHERE id_atribuicao = %s"""

    try:
        cur = connect.cursor()
        cur.execute(sql, (id,))
        
        connect.commit()

        for id_atribuicao in cur.fetchall() :
            print(id_atribuicao)
            return (id_atribuicao)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()


def doDeleteAtribuicao(id):

    connect = myConn()
    sql = """DELETE from clinica.atribuicao WHERE id_atribuicao = %s"""

    try:
        cur = connect.cursor()
        cur.execute(sql, (id,))
        
        connect.commit()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()



