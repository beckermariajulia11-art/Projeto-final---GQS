print("Sistema de cadastro de Pessoas\n");
continuar = "s"
while continuar == "s":
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    email = input("Digite o email: ")
    if idade >= 18:
        situacao = "maior de idade"
    else:
        situacao = "menor de idade"
    print("dados cadastrados")
    print("nome: ", nome)
    print("idade: ", idade)
    print("email: ", email)
    print("situação: ", situacao)

    continuar = input("Deseja cadastrar outra pessoa? (s/n): ").lower()
print("Programa encerrado.")