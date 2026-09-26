# Importação de bibliotecas
import os


restaurantes = [
    {"nome": "Churrascaria do Zé", "categoria": "Rodizio", "aberto": True},
    {"nome": "Pizzaria do João", "categoria": "Pizzaria", "aberto": False},
    {"nome": "Sushi House", "categoria": "Sushi", "aberto": True}
]


# Função para exibir o nome do programa
def nome_do_programa():
    """
    Essa função exibe o nome e a mensagem inicial do programa.

    Inputs:
    -

    Outputs:
    - Exibe o nome do programa no terminal.

    """

    exibir_subtitulo("""
                    ██████╗  █████╗ ██████╗  █████╗ ████████╗██╗███████╗
                    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝
                    ██████╔╝███████║██████╔╝███████║   ██║   ██║█████╗
                    ██╔══██╗██╔══██║██╔══██╗██╔══██║   ██║   ██║██╔══╝
                    ██████╔╝██║  ██║██║  ██║██║  ██║   ██║   ██║███████╗
                    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝

                                    Bem-vindo ao Baratie!
                    """)


# Função para voltar ao menu
def voltar_ao_menu():
    """
    Essa função espera o usuário pressionar Enter e retorna ao menu principal.

    Inputs:
    - Pressionamento da tecla Enter pelo usuário.

    Outputs:
    - Retorna para o menu principal do programa.

    """

    input("\nPressione Enter para Voltar ao Menu... ")
    main()


# Função para exibir o menu
def menu():
    """
    Essa função exibe as opções disponíveis no menu principal.

    Inputs:
    -

    Outputs:
    - Exibe as opções do menu no terminal.

    """

    print("1 - Cadastrar Restaurante")
    print("2 - Listar Restaurantes")
    print("3 - Ativar Restaurante")
    print("4 - Finalizar Programa")


# Função para exibir subtítulos
def exibir_subtitulo(texto):
    """
    Essa função limpa o terminal e exibe um texto ou subtítulo.

    Inputs:
    - texto: texto que será exibido no terminal.

    Outputs:
    - Exibe o texto informado no terminal.

    """

    os.system("cls")
    print(texto)
    print()


# Função para tratar opção inválida
def opcao_invalida():
    """
    Essa função informa ao usuário que a opção escolhida é inválida.

    Inputs:
    -

    Outputs:
    - Exibe uma mensagem de opção inválida e retorna ao menu.

    """

    print("Opção inválida. Por favor, tente novamente.")
    voltar_ao_menu()


# Função para cadastrar restaurante
def cadastrar_restaurante():
    """
    Essa função cadastra um novo restaurante na lista de restaurantes.

    Inputs:
    - Nome do restaurante.
    - Categoria do restaurante.

    Outputs:
    - Adiciona um novo restaurante à lista com status inicial fechado.
    - Exibe uma mensagem confirmando o cadastro.

    """

    exibir_subtitulo("""
                     ██████╗ █████╗ ██████╗  █████╗ ███████╗████████╗██████╗  ██████╗
                    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗
                    ██║     ███████║██║  ██║███████║███████╗   ██║   ██████╔╝██║   ██║
                    ██║     ██╔══██║██║  ██║██╔══██║╚════██║   ██║   ██╔══██╗██║   ██║
                    ╚██████╗██║  ██║██████╔╝██║  ██║███████║   ██║   ██║  ██║╚██████╔╝
                     ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝

                                    Cadastro de Restaurante
                    """)

    nome_do_restaurante = input("Digite o nome do restaurante: ")
    print(f"Nome definido como: {nome_do_restaurante}\n")

    categoria_do_restaurante = input("Digite a categoria do restaurante: ")
    print(f"Categoria definida como: {categoria_do_restaurante}\n")

    print(
        f"Restaurante: {nome_do_restaurante}, da Categoria: "
        f"{categoria_do_restaurante}, Cadastrado com Sucesso!"
    )

    dados_do_restaurante = {
        "nome": nome_do_restaurante,
        "categoria": categoria_do_restaurante,
        "aberto": False
    }

    restaurantes.append(dados_do_restaurante)

    voltar_ao_menu()


# Função para listar restaurantes
def listar_restaurantes():
    """
    Essa função exibe todos os restaurantes cadastrados na lista.

    Inputs:
    - Lista de restaurantes cadastrados.

    Outputs:
    - Exibe o nome, categoria e status de cada restaurante.

    """

    exibir_subtitulo("""
                    ██╗     ██╗███████╗████████╗ █████╗ ██████╗
                    ██║     ██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
                    ██║     ██║███████╗   ██║   ███████║██████╔╝
                    ██║     ██║╚════██║   ██║   ██╔══██║██╔══██╗
                    ███████╗██║███████║   ██║   ██║  ██║██║  ██║
                    ╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝

                                Listar Restaurantes
                    """)

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        status_restaurante = "Aberto" if restaurante["aberto"] else "Fechado"

        print(f"• {nome_restaurante}")
        print(f"• categoria: {categoria_restaurante}")
        print(f"• status: {status_restaurante}")
        print("\n------------------------------\n")

    voltar_ao_menu()


# Função para alternar status do restaurante
def alternar_status_restaurante():
    """
    Essa função altera o status de um restaurante entre aberto e fechado.

    Inputs:
    - Nome do restaurante que terá o status alterado.

    Outputs:
    - Altera o status do restaurante encontrado.
    - Exibe uma mensagem informando se o restaurante foi aberto ou fechado.
    - Informa caso o restaurante não seja encontrado.

    """

    exibir_subtitulo("""
                    ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗
                    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝
                    ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗
                    ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║
                    ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║
                    ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝
                    """)

    nome_do_restaurante = input(
        "Digite o nome do restaurante que deseja alterar o status: "
    )

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["aberto"] = not restaurante["aberto"]

            mensagem_status = (
                f"O restaurante {nome_do_restaurante} foi aberto com sucesso!"
                if restaurante["aberto"]
                else f"O restaurante {nome_do_restaurante} foi fechado com sucesso!"
            )

            print(mensagem_status)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado na lista de restaurantes.")

    restaurante_encontrado = False

    voltar_ao_menu()


# Função para finalizar programa
def finalizar_programa():
    """
    Essa função encerra a execução do programa.

    Inputs:
    -

    Outputs:
    - Exibe uma mensagem informando que o programa foi finalizado.

    """

    exibir_subtitulo("""
                    ██████╗ ██████╗  ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗ █████╗
                    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║██╔══██╗
                    ██████╔╝██████╔╝██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║███████║
                    ██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║██╔══██║
                    ██║     ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║
                    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝

                   ███████╗██╗███╗   ██╗ █████╗ ██╗     ██╗███████╗ █████╗ ██████╗  ██████╗
                   ██╔════╝██║████╗  ██║██╔══██╗██║     ██║╚══███╔╝██╔══██╗██╔══██╗██╔═══██╗
                   █████╗  ██║██╔██╗ ██║███████║██║     ██║  ███╔╝ ███████║██║  ██║██║   ██║
                   ██╔══╝  ██║██║╚██╗██║██╔══██║██║     ██║ ███╔╝  ██╔══██║██║  ██║██║   ██║
                   ██║     ██║██║ ╚████║██║  ██║███████╗██║███████╗██║  ██║██████╔╝╚██████╔╝
                   ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝
                    """)


# Escolha do usuário
def escolha_usuario():
    """
    Essa função recebe a opção escolhida pelo usuário no menu principal.

    Inputs:
    - Número da opção escolhida pelo usuário.

    Outputs:
    - Executa a função correspondente à opção escolhida.
    - Exibe uma mensagem de erro caso ocorra algum problema.

    """

    try:
        escolha = input("Digite a opção desejada: ")

        if escolha == "1":
            cadastrar_restaurante()

        elif escolha == "2":
            listar_restaurantes()

        elif escolha == "3":
            alternar_status_restaurante()
            voltar_ao_menu()

        elif escolha == "4":
            finalizar_programa()

        else:
            opcao_invalida()

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")


# Função principal do programa
def main():
    """
    Essa função inicia o programa e organiza a execução do menu principal.

    Inputs:
    -

    Outputs:
    - Exibe o nome do programa.
    - Exibe o menu.
    - Aguarda a escolha do usuário.

    """

    nome_do_programa()
    menu()
    escolha_usuario()


# Ponto de entrada do programa
if __name__ == "__main__":
    main()