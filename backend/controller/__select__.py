import sys  

#caminho para conexao
sys.path.insert(0, 'caminho para conexão')
from __connection__ import myConn


def doSelect( conn ) :
    cur = conn.cursor()

    cur.execute("SELECT nome, sexo, data_nasc, email FROM clinica.pessoa")

    for nome, sexo, data_nasc, email in cur.fetchall() :
        print( nome, sexo, data_nasc, email )

    cur.close()

connect = myConn()

doSelect(connect)