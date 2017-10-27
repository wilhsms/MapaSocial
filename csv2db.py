import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import config


dados_estacoes = pd.read_csv("estacoes_es.csv", encoding='latin-1',sep=',')
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
df = pd.DataFrame(dados_estacoes)
df.to_sql('estacao_meteorologica', engine,  if_exists='replace')
