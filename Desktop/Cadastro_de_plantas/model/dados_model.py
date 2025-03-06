import mariadb


class DadosModel:
    def __init__(self):
        self.conexao = mariadb.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="rootpassword",
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

    def buscar_dados(self):
        self.cursor.execute("select * from dados")
        return self.cursor.fetchall()