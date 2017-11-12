import sqlite3

class Usuario():
    def __init__(self, nome, email, senha, genero, idade, profissao, cidade, usuarios):
        usuarios = []
        self.nome = nome
        self.email = email
        self.senha = senha
        self.genero = genero
        self.idade = idade
        self.profissao = profissao
        self.cidade = cidade

    def inserir(self):
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
            INSERT INTO tb_usuario(nome, email, senha, genero, idade, profissao, cidade)
            VALUES (self.nome, self.email, self.senha, self.genero, self.idade, self.profissao, self.cidade);
            """)

    def listar(usuario):
        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM usuario """)

        for linha in cursor.fetchall():
            self.nome = nome
            print(linha)
            usuario = Usuario(nome, email, senha, genero, idade, profissao, cidade, usuarios)
            usuarios.append(usuario)

        return usuarios



conn.commit()

print("Usuário cadastrado com sucesso")

conn.close()
