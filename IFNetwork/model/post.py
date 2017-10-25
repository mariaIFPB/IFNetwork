import sqlite3
conn = sqlite3.connect("IFNetwork.db")
cursor = conn.cursor()

texto_post = input("Qual a mensagem? ")
id_usuario = int(input("Quem envia? "))
visibilidade = input("Pra quem envia? ")

cursor.execute("""
INSERT INTO post(texto_post, id_usuario, visibilidade) VALUES (?, ?, ?);
""", (texto_post, id_usuario, visibilidade))

cursor.execute("""
SELECT * FROM post """)

for linha in cursor.fetchall():
    print(linha)

conn.commit()

conn.close()
