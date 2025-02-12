import mysql.connector


class DadosModel:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="plantas_db",
        )
        self.cursor = self.conexao.cursor()

    def inserir_dados(self, umidade, temperatura, luminosidade):
        sql = (
            "INSERT INTO dados (umidade, temperatura, luminosidade) VALUES (%s, %s, %s)"
        )
        valores = (float(umidade), float(temperatura), int(luminosidade))
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        return self.cursor.lastrowid

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()
