import sqlite3

class Usuario():
    def __init__(self, nome, email, telefone, senha, genero, idade, profissao, cidade, usuarios=[]):
        self.usuarios = usuarios
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.genero = genero
        self.idade = idade
        self.profissao = profissao
        self.cidade = cidade

    def inserirUser(self):
        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tb_usuario(nome, email, telefone, senha, genero, idade, profissao, cidade)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (self.nome, self.email, self.telefone, self.senha, self.genero, self.idade, self.profissao, self.cidade))
        conn.commit()
        conn.close()
        
    def listar(self):
        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM usuario """)

        for linha in cursor.fetchall():
            nome = linha[1]
            email = linha[2]
            telefone = linha[3]
            senha = linha[4]
            genero = linha[5]
            idade = linha[6]
            profissao = linha[7]
            cidade = linha[8]
            usuario = Usuario(nome, email, senha, genero, idade, profissao, cidade)
            self.usuarios.append(usuario)
            conn.commit()
            conn.close()
            
        return self.usuarios

    def atualizar_fone_email(self):
        emailAntigo = self.email
        opcao = int(input("\ndeseja mudar seu email?\n"
                      "1 - sim"
                      "2 - não")
        if (opcao == 1):
            self.email = input("informe o novo email: ")

        opcao = int(input("\ndeseja mudar seu numero de telefone?\n"
                      "1 - sim"
                      "2 - não")
        if (opcao == 1):
            self.telefone = input('informe o novo telefone: ')

        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()

        cursor.execute("""
            UPDADE tb_usuario
            SET email = ?, telefone = ?
            WHERE email = ?
        """, (self.email, self.telefone, emailAntigo))
        
    def deletar(self, email):
        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM tb_usuario WHERE id = ?
            """, (email))
        conn.commit()
        conn.close()
