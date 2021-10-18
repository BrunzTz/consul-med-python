import sys
import psycopg2

#colocar o caminho da pasta onde se localiza a conexão no sistema
sys.path.insert(0, 'caminho para conexão')
sys.path.insert(1, 'caminho para model')

from __connection__ import myConn
from __pessoa__ import *

def doInsertPessoa(conn, nome, endereco, telefone, cpf, sexo, data_nasc, email) :

    
    sql = """INSERT INTO clinica.pessoa (nome, endereco, telefone, cpf, sexo, data_nasc, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    try:
        cur = conn.cursor()
        cur.execute(sql, (nome, endereco, telefone, cpf, sexo, data_nasc, email))
        
        conn.commit()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return sexo
    
pessoa = Pessoa('teste5', 'teste endereço2', '3444423', '9215643', 'F', '2021-01-01', 'teste3@email.com')

connect = myConn()
doInsertPessoa(connect, pessoa.getNome(), pessoa.getEndereco(), pessoa.getTelefone(), pessoa.getCPF(), pessoa.getSexo(), pessoa.getData_nasc(), pessoa.getEmail())
print(pessoa.getEmail())