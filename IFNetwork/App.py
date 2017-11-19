import sqlite3

conn = sqlite3.connect('IFNetwork.db')
cursor = conn.cursor()

# Criando as tabelas: usuario, mensagem, post, amizade, amigo_usuario

cursor.execute("""
    CREATE TABLE tb_usuario(
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        senha VARCHAR(15) NOT NULL,
        genero VARCHAR(15),
        idade INTEGER,
        profissao VARCHAR(50),
        cidade VARCHAR(50),
        );
        """)

cursor.execute("""
    CREATE TABLE tb_amizade(
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        data_amizade TEXT
        );
        """)

cursor.execute("""
    CREATE TABLE tb_amigo_usuario(
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        id_usuario1 INTEGER,
        id_usuario2 INTEGER,
        );
        """)

cursor.execute("""
    CREATE TABLE tb_mensagem(
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        id_remetente INTEGER FOREIGN KEY,
        id_destinatario INTEGER FOREIGN KEY,
        texto_msg(255),
        horario_MSG DATE)
        );
        """)

cursor.execute("""
    CREATE TABLE tb_post(
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        id_usuario INTEGER NOT NULL,
        texto_post VARCHAR(150) NOT NULL,
        visibilidade VARCHAR(250)
        );
        """)

conn.close()
