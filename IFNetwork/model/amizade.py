import sqlite3
from datetime import *

class Amizade():
    def __init__(self, dataAmizde):
        self.dataAmizade = dataAmizde

    dataAmizade = datetime('now')

    conn = sqlite3.connect("IFNetwork.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tb_amizade(data_amizade) VALUES(dataAmizade);
    """)

    conn.commit()
    
    print("amizade funciona.")

    conn.close()
