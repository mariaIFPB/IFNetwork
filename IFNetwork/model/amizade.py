import sqlite3
from datetime import *
from model.usuario import Usuario
from model.amigo_usuario import Amigo_Usuario

#Classe relacionada a Amizade do usuário. 

class Amizade():
    
    def __init__(self, dataAmizde, email1, email2):
        self.dataAmizade = dataAmizade
        self.email1 = email1
        self.email2 = email2
    
    def solicitarAmizade(self):
        pass
    
    def AmigoUsuario(self):
        
        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()

        email1 = input("informe seu email: ")
        email2 = input("informe o email do seu amigo: ")

        cursor.execute("""
        INSERT INTO tb_amigo_usuario(email1, email2)
        VALUES (?,?); """, (email1, email2))

        dataAmizade = datetime('now')
        
        cursor.execute("""
            INSERT INTO tb_amizade(data_amizade) VALUES(dataAmizade);
            """)
        
        conn.commit()
        conn.close()
    
    def excluirAmizade(self):
        
        #excluindo uma amizade a partir do email do amigo que deseja excluir.
        
        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()
        email = self.email
        cursor.execute("""
            DELETE FROM tb_amizade
            WHERE email = ?
            """, (email))
        conn.commit()
        conn.close()
    
    def listarAmigos():
        pass
    
    def buscarAmigo():
        pass
    
    conn.commit()
    
    print("amizade funciona.")

    conn.close()
