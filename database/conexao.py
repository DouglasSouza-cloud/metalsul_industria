import os
import psycopg # POSTGRESQL
from dotenv import load_dotenv

load_dotenv() # CARREGA AUTOMATICAMENTE AS VARIÁVEIS DE AMBIENTE DO ARQUIVO .env

class Conexao:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")

        self.conexao = psycopg.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname=self.database
        )
        self.cursor = self.conexao.cursor()
    def commit(self):
        self.conexao.commit()

    def rollback(self):
        self.conexao.rollback()

    def close(self):
        self.cursor.close()
        self.conexao.close()