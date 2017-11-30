import sqlite3

class Post():

    def __init__(self, texto_post, email_usuario, visibilidade):
        self.texto_post = texto_post
        self.email_usuario = email_usuario
        self.visibilidade = visibilidade

    def visibilidadePost(self):
        #resolver se será público, só para amigos, só para um amigo.
        pass
    
    def postar(self):
        feed = []
        conn = sqlite3.connect("IFNetwork.db")
        cursor = conn.cursor()

        texto_post = input("Qual a mensagem? ")
        email_usuario = input("Quem envia? ")
        visibilidade = visibilidadePost(self)
        post = Post(texto_post, email_usuario, visibilidade)
        feed.append(post)
        
        cursor.execute("""
        INSERT INTO tb_post(texto_post, email_usuario, visibilidade) VALUES (?, ?, ?);
        """, (texto_post, email_usuario, visibilidade))

        cursor.execute(""" SELECT * FROM Post """)

        for linha in cursor.fetchall():
            print(linha)

        conn.commit()
        conn.close()
