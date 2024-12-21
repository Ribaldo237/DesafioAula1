import json

def criar_arquivo_json():
    usuarios = [
        {"nome": "João", "idade": 25},
        {"nome": "Maria", "idade": 30}
    ]
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)
    print("Arquivo JSON criado com sucesso!")

def adicionar_usuario():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
        
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        novo_usuario = {"nome": nome, "idade": idade}

        usuarios.append(novo_usuario)

        with open("usuarios.json", "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)
        print("Usuário adicionado com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo primeiro.")
    except ValueError:
        print("Por favor, insira uma idade válida.")

def exibir_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        print("Usuários registrados:")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}")
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo primeiro.")
#Essa implementação faz com que tenha a opção de pesquisar por um usuario pelo seu nome
# def pesquisar_usuario():
#     try:
#         # Abre o arquivo JSON para ler os usuários
#         with open("usuarios.json", "r") as arquivo:
#             usuarios = json.load(arquivo)
        
#         # Solicita ao usuário o nome que deseja pesquisar
#         nome_pesquisar = input("Digite o nome do usuário que deseja pesquisar: ")

#         # Percorre a lista de usuários para encontrar o nome
#         usuario_encontrado = False
#         for usuario in usuarios:
#             if usuario['nome'].lower() == nome_pesquisar.lower():
#                 # Exibe as informações do usuário encontrado
#                 print(f"Usuário encontrado: Nome: {usuario['nome']}, Idade: {usuario['idade']}")
#                 usuario_encontrado = True
#                 break

#         # Se não encontrar o usuário
#         if not usuario_encontrado:
#             print(f"Usuário {nome_pesquisar} não encontrado.")
#     except FileNotFoundError:
#         print("Arquivo não encontrado. Crie o arquivo primeiro.")
#Essa implementação atualiza a idade do usuario que muda ano apos ano
# def atualizar_idade_usuario():
#     try:
#         # Abre o arquivo JSON para ler os usuários
#         with open("usuarios.json", "r") as arquivo:
#             usuarios = json.load(arquivo)
        
#         # Solicita o nome do usuário cuja idade será atualizada
#         nome_atualizar = input("Digite o nome do usuário que deseja atualizar a idade: ")

#         # Percorre a lista de usuários para encontrar o nome
#         usuario_encontrado = False
#         for usuario in usuarios:
#             if usuario['nome'].lower() == nome_atualizar.lower():
#                 # Solicita a nova idade
#                 try:
#                     nova_idade = int(input(f"Digite a nova idade para {nome_atualizar}: "))
#                     usuario['idade'] = nova_idade  # Atualiza a idade do usuário
#                     print(f"A idade de {nome_atualizar} foi atualizada para {nova_idade} anos.")
#                 except ValueError:
#                     print("Idade inválida! Por favor, insira um número.")
#                 usuario_encontrado = True
#                 break

#         if not usuario_encontrado:
#             print(f"Usuário {nome_atualizar} não encontrado.")

#         # Regrava o arquivo JSON com a lista atualizada
#         with open("usuarios.json", "w") as arquivo:
#             json.dump(usuarios, arquivo, indent=4)

#     except FileNotFoundError:
#         print("Arquivo não encontrado. Crie o arquivo primeiro.")
#Essa implementação faz que seja possivel remover um usuario, foi a que eu escolhi.
def remover_usuario():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
        
        nome_remover = input("Digite o nome do usuário que deseja remover: ")

        # Encontrar e remover o usuário
        usuario_encontrado = False
        for usuario in usuarios:
            if usuario['nome'].lower() == nome_remover.lower():
                usuarios.remove(usuario)
                usuario_encontrado = True
                print(f"Usuário {nome_remover} removido com sucesso!")
                break

        if not usuario_encontrado:
            print(f"Usuário {nome_remover} não encontrado.")

        # Regravar a lista no arquivo
        with open("usuarios.json", "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)

    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo primeiro.")

# Menu interativo
print("Bem-vindo ao Gerenciador de Usuários JSON!")
while True:
    print("\nEscolha uma opção:")
    print("1. Criar arquivo JSON")
    print("2. Adicionar usuário")
    print("3. Exibir usuários")
    print("4. Remover usuário")
    print("5. Sair")

    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        criar_arquivo_json()
    elif opcao == "2":
        adicionar_usuario()
    elif opcao == "3":
        exibir_usuarios()
    elif opcao == "4":
        remover_usuario()
    elif opcao == "5":
        print("Saindo... Até mais!")
        break
    else: #Esse else pode ser removido sem problema, que nao afetara o codigo.
        print("Opção inválida. Tente novamente.")
