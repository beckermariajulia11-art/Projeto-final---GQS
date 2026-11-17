"""Programa para cadastro de pessoas. Uso didático na disciplina de GQS."""

from cadastro import CadastroPessoas


def exibir_menu():
    """Exibe o menu principal e devolve a opção digitada, como inteiro."""
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Analisar pessoa")
    print("6 - Sair")
    return int(input("Escolha uma opcao: "))


def cadastrar_pessoa(cadastro):
    """Lê os dados de uma nova pessoa e a cadastra."""
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    email = input("Informe o email: ")

    cadastro.cadastrar(nome, idade, email)

    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")


def exibir_pessoa(pessoa):
    """Exibe os dados de uma pessoa."""
    print("Nome: " + pessoa.getNome())
    print("Idade: " + str(pessoa.getIdade()))
    print("E-mail: " + pessoa.getEmail())
    if pessoa.getIdade() >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")


def consultar_pessoa(cadastro):
    """Consulta uma pessoa pelo nome."""
    procurado = input("Nome para consultar: ")
    pessoa = cadastro.buscarPorNome(procurado)

    if pessoa is None:
        print("Nao encontrado")
    else:
        exibir_pessoa(pessoa)


def alterar_pessoa(cadastro):
    """Altera os dados de uma pessoa."""
    procurado = input("Nome para alterar: ")
    pessoa = cadastro.buscarPorNome(procurado)

    if pessoa is None:
        print("Nao encontrado")
    else:
        novo_nome = input("Novo nome: ")
        nova_idade = int(input("Nova idade: "))
        novo_email = input("Novo e-mail: ")
        cadastro.alterar(procurado, novo_nome, nova_idade, novo_email)

        print("Pessoa alterada!")
        exibir_pessoa(pessoa)


def listar_pessoas(cadastro):
    """Lista todas as pessoas cadastradas."""
    pessoas = cadastro.listar()

    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada")

    for pessoa in pessoas:
        exibir_pessoa(pessoa)
        print("-------------------------")

    print("Total: " + str(len(pessoas)))


def analisar_faixa_etaria(idade):
    """Informa a faixa etária."""
    if idade < 12:
        print("Faixa etaria: Crianca")
    elif idade < 18:
        print("Faixa etaria: Adolescente")
    elif idade < 30:
        print("Faixa etaria: Adulto jovem")
    elif idade < 60:
        print("Faixa etaria: Adulto")
    else:
        print("Faixa etaria: Idoso")


def analisar_email(email):
    """Informa a situação do e-mail e o provedor."""
    if email == "":
        print("Cadastro incompleto: sem e-mail")
    elif "@" not in email:
        print("E-mail invalido")
    elif email.endswith("@gmail.com"):
        print("Provedor: Gmail")
    elif email.endswith("@outlook.com"):
        print("Provedor: Outlook")
    elif email.endswith("@hotmail.com"):
        print("Provedor: Hotmail")
    elif email.endswith("@utfpr.edu.br"):
        print("Provedor: UTFPR")
    else:
        print("Provedor: Outro")


def analisar_contato(idade, email):
    """Informa a condição para contato."""
    if idade >= 18 and email != "":
        print("Cadastro apto para contato")
    elif idade >= 18 and email == "":
        print("Maior de idade sem contato")
    elif idade < 18 and email != "":
        print("Menor de idade com contato")
    else:
        print("Menor de idade sem contato")


def analisar_pessoa(cadastro):
    """Analisa faixa etária, e-mail e contato de uma pessoa."""
    procurado = input("Nome para analisar: ")
    pessoa = cadastro.buscarPorNome(procurado)

    if pessoa is None:
        print("Pessoa nao encontrada")
    else:
        analisar_faixa_etaria(pessoa.getIdade())
        analisar_email(pessoa.getEmail())
        analisar_contato(pessoa.getIdade(), pessoa.getEmail())


def executar():
    """Executa o menu principal da aplicação."""
    cadastro = CadastroPessoas()
    op = 0

    while op != 6:
        op = exibir_menu()
        if op == 1:
            cadastrar_pessoa(cadastro)
        elif op == 2:
            consultar_pessoa(cadastro)
        elif op == 3:
            alterar_pessoa(cadastro)
        elif op == 4:
            listar_pessoas(cadastro)
        elif op == 5:
            analisar_pessoa(cadastro)
        elif op == 6:
            print("Saindo...")
        else:
            print("Opcao invalida")

    print("Fim do programa")


if __name__ == "__main__":
    executar()
