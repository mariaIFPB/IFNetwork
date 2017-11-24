import sqlite3

class Mensagem():
  
    def __init__(self, texto, email_remetente, email_destinatario):
        self.texto = texto
        self.email_remetente = email_remetente
        self.email_destinatario = email_destinatario

    
    def enviarMsg(self):
      
        conn = sqlite3.connect("IFNetwork.db")
        cursor = conn.cursor()

        texto = input("Qual a mensagem? ")
        email_remetente = input("Quem envia? ")
        email_destinatario = input("Pra quem envia? ")
        
        #mensagem = Mensagem(texto, email_remetente, email_destinatario)
        
        cursor.execute("""
        INSERT INTO tb_mensagem(horario) VALUES (datetime('now'));
        INSERT INTO tb_mensagem(texto, id_remetente, id_destinatario) VALUES (?, ?, ?);
        """, (texto, email_remetente, email_destinatario))

        conn.commit()

        conn.close() 
