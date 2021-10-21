import sys
import psycopg2

#colocar o caminho da pasta onde se localiza a conexão no sistema
sys.path.insert(0, 'C:/Users/AULA/OneDrive/Área de Trabalho/consul-med-python/backend/database/')
sys.path.insert(1, 'C:/Users/AULA/OneDrive/Área de Trabalho/consul-med-python/backend/model/')

from __connection__ import myConn
from __pessoa__ import Pessoa

connect = myConn()
