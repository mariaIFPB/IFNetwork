import sqlite3

class Amigo_Usuario():
    def __init__ (email1, email2):
        self.email1 = email1
        self.email2 = email2

        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()

        email1 = int(input("informe seu email: "))
        email2 = int(input("informe o email do seu amigo: "))

        cursor.execute("""
        INSERT INTO amigo_usuario(email1, email2)
        VALUES (?,?); """, (email1, email2))

        conn.commit()
        conn.close()
