import sys
import psycopg2

#colocar o caminho da pasta onde se localiza a conexão no sistema
sys.path.insert(0, 'C:/Users/AULA/OneDrive/Área de Trabalho/consul-med-python/backend/database/')

from __connection__ import myConn

connect = myConn()

class Pessoa:

    def __init__(self, nome, endereco, telefone, cpf, sexo, data_nasc, email):

        self.nome = nome,
        self.endereco = endereco,
        self.telefone = telefone,
        self.cpf = cpf,
        self.sexo = sexo,
        self.data_nasc = data_nasc,
        self.email = email
    
    def getNome(self):

        str = ''
        for item in self.nome:
            str = str + item
            return str

    def getEndereco(self):

        str = ''
        for item in self.endereco:
            str = str + item
            return str

    def getTelefone(self):

        str = ''
        for item in self.telefone:
            str = str + item
            return str

    def getCPF(self):

        str = ''
        for item in self.cpf:
            str = str + item
            return str

    def getSexo(self):

        str = ''
        for item in self.sexo:
            str = str + item
            return str

    def getData_nasc(self):

        str = ''
        for item in self.data_nasc:
            str = str + item
            return str

    def getEmail(self):

        return self.email


def doInsertPessoa(nome, endereco, telefone, cpf, sexo, data_nasc, email) :

    connect = myConn()
    sql = """INSERT INTO clinica.pessoa (nome, endereco, telefone, cpf, sexo, data_nasc, email) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING pessoa.id_pessoa, pessoa.nome"""

    try:
        cur = connect.cursor()
        cur.execute(sql, (nome, endereco, telefone, cpf, sexo, data_nasc, email))
        
        connect.commit()
        for id_pessoa, nome in cur.fetchall() :
            print(id_pessoa, nome)
            return id_pessoa

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()


def doSelectSinglePessoa(id):

    connect = myConn()
    sql = """SELECT nome, sexo, data_nasc, email FROM clinica.pessoa WHERE id_pessoa = %s """

    try:
        cur = connect.cursor()
        cur.execute(sql, (id,))
        
        connect.commit()

        for nome, sexo, data_nasc, email in cur.fetchall() :
            print(nome, sexo, data_nasc, email)

        cur.close()

        

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()

def doSelectAllPessoa():

    connect = myConn()
    sql = """SELECT id_pessoa, nome, sexo, data_nasc, email FROM clinica.pessoa"""

    try:
        cur = connect.cursor()
        cur.execute(sql)
        
        connect.commit()

        for id_pessoa, nome, sexo, data_nasc, email in cur.fetchall() :
            print(id_pessoa, nome, sexo, data_nasc, email)


        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()

def doDeletePessoa(id):

    connect = myConn()
    sql = """DELETE FROM clinica.pessoa WHERE id = %s """

    try:
        cur = connect.cursor()
        cur.execute(sql, id)
        
        connect.commit()

        cur.close()

        result = "Deletado com sucesso!"

        return result

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()

def doUpdatePessoa(id, nome, sexo, email, telefone, endereco):

    connect = myConn()
    sql = """UPDATE clinica.pessoa SET pessoa.nome = %s, SET pessoa.sexo = %s, SET pessoa.email = %s, SET pessoa.telefone = %s, SET pessoa.endereco = %s WHERE id = %s"""

    try:
        cur = connect.cursor()
        cur.execute(sql, (nome, sexo, email, telefone, endereco, id))
        
        connect.commit()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connect is not None:
            connect.close()