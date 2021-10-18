import sys
import psycopg2

#colocar o caminho da pasta onde se localiza a conexão no sistema
sys.path.insert(0, 'caminho para conexão')

from __connection__ import myConn

def doDeletePessoa(conn, id):

    sql = """DELETE FROM clinica.pessoa WHERE id_pessoa = %s"""
    try:
        cur = conn.cursor()
        cur.execute(sql, (id,))
        
        conn.commit()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

connect = myConn()

doDeletePessoa(connect, 28)