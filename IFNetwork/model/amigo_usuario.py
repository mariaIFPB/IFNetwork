import sqlite3
conn = sqlite3.connect('IFNetwork.db')
cursor = conn.cursor()

#usando o id para identificar as pessoas
id_usuario1 = int(input("informe seu nome: "))
id_usuario2 = int(input("informe seu email: "))

cursor.execute("""
INSERT INTO amigo_usuario(id_usuario1, id_usuario2)
VALUES (?,?); """, (id_usuario1, id_usuario2))

conn.commit()

print("isso funciona.")

conn.close()
