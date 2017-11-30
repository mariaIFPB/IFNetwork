import sqlite3

class Usuario():
    def __init__(self, nome, email, telefone, senha, genero, idade, profissao, cidade, usuarios=[]):
        if usuarios is None:
            usuarios = []
        self.usuarios = usuarios
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.genero = genero
        self.idade = idade
        self.profissao = profissao
        self.cidade = cidade

    def inserirUsuario(self):
        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tb_usuario(nome, email, telefone, senha, genero, idade, profissao, cidade)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (self.nome, self.email, self.telefone, self.senha, self.genero, self.idade, self.profissao, self.cidade))
        conn.commit()
        conn.close()
        
    def listarUsuarios(self):
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
            usuario = Usuario(nome, email, telefone, senha, genero, idade, profissao, cidade)
            self.usuarios.append(usuario)
            conn.commit()
            conn.close()
            
        return self.usuarios

    #por enquanto atualizando apenas o telefone e o email.
    
    def atualizar_fone_email(self):
        emailAntigo = self.email
        opcao = int(input("\ndeseja mudar seu email?\n"
                      "1 - sim"
                      "2 - não"))
        if (opcao == 1):
            self.email = input("informe o novo email: ")

        opcao = int(input("\ndeseja mudar seu numero de telefone?\n"
                      "1 - sim"
                      "2 - não"))
        if (opcao == 1):
            self.telefone = input('informe o novo telefone: ')

        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()

        cursor.execute("""
            UPDADE tb_usuario
            SET email = ?, telefone = ?
            WHERE email = ?
        """, (self.email, self.telefone, emailAntigo))
        
    def deletarUsuario(self):
        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()    
        email = input("informe o email da conta a ser deletada: ")
        senhaD = input("informe a senha: ")
        
        if (senhaD == self.senha):
            cursor.execute("""
                DELETE FROM tb_usuario 
                WHERE email = ?
                """, (email))
            conn.commit()
            conn.close()

