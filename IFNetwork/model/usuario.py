import sqlite3

conn = sqlite3.connect('IFNetwork.db')
cursor = conn.cursor()

nome = input("informe seu nome: ")
email = input("informe seu email: ")
senha = input("informe a senha: ")
genero = input("informe o seu gênero: ")
idade = int(input("informe sua idade: "))
profissao = input("informe sua profissão: ")
cidade = input("informe sua cidade: ")

cursor.execute("""
INSERT INTO usuario(nome, email, senha, genero, idade, profissao, cidade)
VALUES (?, ? ,? ,? ,? ,? ,?);
""", (nome, email, senha, genero, idade, profissao, cidade))

conn.commit()

print("Usuário cadastrado com sucesso")

conn.close()
