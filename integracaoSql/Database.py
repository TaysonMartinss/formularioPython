import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.drive = os.getenv('DB_DRIVER')
        self.server = os.getenv('DB_SERVER')
        self.database = os.getenv('DB_NAME')
        self.uid = os.getenv('DB_USER')
        self.pwd = os.getenv('DB_PASSWORD')
        self.conn = None



    def connect(self):
        self.conn = pyodbc.connect(
            f'DRIVER={self.drive};'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            f'UID={self.uid};'
            f'PWD={self.pwd};'
        )


    def insert_data(self, nome, email, telefone, enderco, cpf):
        if self.conn is None:
            self.connect()

        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO CADASTRO (NOME, EMAIL, TELEFONE, ENDERECO, CPF)
        VALUES (?, ?, ?, ?, ?)
        """, (nome, email, telefone, enderco, cpf))
        self.conn.commit()


    def fetch_data(self):
        if self.conn is None:
            self.connect()


        cursor = self.conn.cursor()
        cursor.execute("SELECT nome, Email, Telefone, Endereco,CPF FROM CADASTRO")
        data = cursor.fetchall()
        return data

    def close(self):
        if self.conn is not None:
            self.conn.close()