import sqlite3
import datetime

class Amizade():

    conn = sqlite3.connect("IFNetwork.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO amizade(data_amizade) VALUES(datetime('now'));
    """)

    conn.commit()

    print("amizade funciona.")

    conn.close()
