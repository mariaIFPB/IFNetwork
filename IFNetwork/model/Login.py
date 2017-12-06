import mysql.connector

config = {
  ' usuário ' : ' root ' ,
  ' senha ' : ' ' ,
  ' host ' : ' 127.0.0.1 ' ,
  ' banco de dados ' : ' IFNet ' ,
  ' raise_on_warnings ' : True
}

class Login ():
  db = MySQLdb.connect(**config)
  cursor = db.cursor()
  cursor.execute("SELECT * FROM tb_login")
  dados = cursor.fetchall()

  for linha in result:
    if nome == linha[0]:
	    if senha == linha[1]:
        print("usuário logado.")
