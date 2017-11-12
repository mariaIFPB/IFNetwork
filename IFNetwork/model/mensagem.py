import sqlite3

class Mensagem ():
  
    def __init__(texto, remetente, destinatario, chat):
        self.texto = texto
        self.remetente = remetente
        self.destinatario = destinatario
        chat = []
    
    def enviarMsg():
      
        conn = sqlite3.connect("IFNetwork.db")
        cursor = conn.cursor()

        texto = input("Qual a mensagem? ")
        remetente = input("Quem envia? "))
        destinatario = input("Pra quem envia? "))
        
        mensagem = Mensagem(texto, remetente, destinatario)
        chat.append(mensagem)
        
        cursor.execute("""
        INSERT INTO tb_mensagem(horario) VALUES (datetime('now'));
        INSERT INTO tb_mensagem(texto, id_remetente, id_destinatario) VALUES (?, ?, ?);
        """, (texto, remetente, destinatario))

    conn.commit()

    conn.close()
