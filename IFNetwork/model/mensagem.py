import sqlite3
conn = sqlite3.connect("IFNetwork.db")
cursor = conn.cursor()

texto = input("Qual a mensagem? ")
id_remetente = int(input("Quem envia? "))
id_destinatario = int(input("Pra quem envia? "))

cursor.execute("""
INSERT INTO mensagem(horario) VALUES (datetime('now'));
INSERT INTO mensagem(texto, id_remetente, id_destinatario) VALUES (?, ?, ?);
""", (texto, id_remetente, id_destinatario))

conn.commit()

conn.close()
