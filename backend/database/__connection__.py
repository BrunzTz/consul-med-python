import psycopg2 as db_connect

def myConn():
    host_name="consul-med.postgres.database.azure.com"
    db_user="brunorocha@consul-med"
    db_password="bruno@1999"
    db_name="postgres"
    return db_connect.connect(host=host_name,user=db_user,password=db_password,database=db_name)
