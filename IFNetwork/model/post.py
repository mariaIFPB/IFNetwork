import sqlite3

class Post():

    def __init__ (texto_post, id_usuario, visibilidade):
        self.texto_post = texto_post
        self.id_usuario = id_usuario
        self.visibilidade = visibilidade

    def postar():
        conn = sqlite3.connect("IFNetwork.db")
        cursor = conn.cursor()

        texto_post = input("Qual a mensagem? ")
        id_usuario = int(input("Quem envia? "))
        visibilidade = input("Pra quem envia? ")

        cursor.execute("""
        INSERT INTO tb_post(texto_post, id_usuario, visibilidade) VALUES (?, ?, ?);
        """, (texto_post, id_usuario, visibilidade))

        cursor.execute(""" SELECT * FROM Post """)

        for linha in cursor.fetchall():
            print(linha)

conn.commit()

conn.close()
