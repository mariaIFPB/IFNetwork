import sqlite3

# Criando as tabelas: usuario, mensagem, post, amizade, amigo_usuario

try:

    conn = sqlite3.connect('IFNetwork.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE tb_usuario(
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            senha VARCHAR(15) NOT NULL,
            genero VARCHAR(15),
            idade INTEGER,
            profissao VARCHAR(50),
            cidade VARCHAR(50)
            );
            """)

    cursor.execute("""
        CREATE TABLE tb_amizade(
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            data_amizade DATE
            );
            """)

    cursor.execute("""
        CREATE TABLE tb_amigo_usuario(
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            email1 VARCHAR(100) NOT NULL,
            email2 VARCHAR(100) NOT NULL,
            email1 FOREIGN KEY,
            REFERENCES usuario(email),
            email2 FOREIGN KEY,
            REFERENCES usuario(email)
            );
            """)

    cursor.execute("""
        CREATE TABLE tb_mensagem(
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            email_remetente VARCHAR(100) NOT NULL ,
            email_destinatario VARCHAR(100) NOT NULL,
            texto_msg(255),
            horario_MSG DATE
            email_remetente FOREIGN KEY,
            REFERENCES usuario(email),
            email_destinatario FOREIGN KEY,
            REFERENCES usuario(email)
            );
            """)

    cursor.execute("""
        CREATE TABLE tb_post(
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            email_usuario VARCHAR(100) NOT NULL,
            texto_post VARCHAR(150) NOT NULL,
            visibilidade VARCHAR(250),
            email_usuario FOREIGN KEY,
            REFERENCES usuario(email)
            );
            """)
    conn.close()

except sqlite3.OperationalError:
    print("o banco de dados ja existe.")
