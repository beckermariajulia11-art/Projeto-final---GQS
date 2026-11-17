"""Gerenciamento do cadastro de pessoas."""

from pessoa import Pessoa


class CadastroPessoas:
    """Mantém e gerencia o conjunto de pessoas cadastradas."""

    def __init__(self):
        self.__pessoas = []

    def cadastrar(self, nome, idade, email):
        """Cria uma Pessoa, guarda no cadastro e a devolve."""
        pessoa = Pessoa(nome, idade, email)
        self.__pessoas.append(pessoa)
        return pessoa

    def buscarPorNome(self, nome):
        """Devolve a primeira pessoa com esse nome, ou None se não existir."""
        for pessoa in self.__pessoas:
            if pessoa.getNome() == nome:
                return pessoa
        return None

    def listar(self):
        """Devolve as pessoas cadastradas."""
        return self.__pessoas

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        """Altera os dados da pessoa com esse nome; devolve None se não existir."""
        pessoa = self.buscarPorNome(nome)

        if pessoa is None:
            return None

        pessoa.setNome(novo_nome)
        pessoa.setIdade(nova_idade)
        pessoa.setEmail(novo_email)

        return pessoa
