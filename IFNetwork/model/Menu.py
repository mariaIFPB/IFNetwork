from Usuario import Usuario


para inserir novo usuario:

opcao = int(inpt("seja bem vindo!\n"
      "\n opções:\n"
      "1 - criar novo usuário"
      "2 - deletar usuário")

if (opcao == 1):
    nome = input("informe seu nome: ")
    email = input("informe seu email: ")
    senha = input("informe a senha: ")
    genero = input("informe o seu gênero: ")
    idade = int(input("informe sua idade: "))
    profissao = input("informe sua profissão: ")
    cidade = input("informe sua cidade: ")
    u = Usuario(nome, email, senha, genero, idade, profissao, cidade, usuarios)
    u.inserirUser()

