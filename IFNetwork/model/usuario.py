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
        conn.commit()
        conn.close()
        
    def listar(usuario):
        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM usuario """)

        for linha in cursor.fetchall():
            nome = linha[1]
            email = linha[2]
            senha = linha[3]
            profissao = linha[4]
            sexo = linha[5]
            usuario = Usuario(nome, email, senha, genero, idade, profissao, cidade, usuarios)
            usuarios.append(usuario)
            conn.commit()
            conn.close()
            
        return usuarios

    def atualizar_fone_email(self, id):
        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()
        self.novo_fone = input('Fone: ')
        self.novo_email = input('Email: ')
        cursor.execute("""
        UPDATE tb_usuario
        SET fone = ?
        WHERE id = ?
        """, (self.novo_fone, id,))
        cursor.execute("""
        UPDATE tb_usuario
        SET email = ?
        WHERE id = ?
        """, (self.novo_email, id,))
        print("Dados atualizados com sucesso.")
        conn.commit()
        conn.close()
        
    def deletar(self, id):
        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM tb_usuario WHERE id = ?
            """, (id))
        conn.commit()
        conn.close()
