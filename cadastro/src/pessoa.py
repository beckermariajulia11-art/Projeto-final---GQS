"""Classe Pessoa."""


class Pessoa:
    """Representa uma pessoa com nome, idade e e-mail (estado privado)."""

    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    def getNome(self):
        """Devolve o nome."""
        return self.__nome

    def getIdade(self):
        """Devolve a idade."""
        return self.__idade

    def getEmail(self):
        """Devolve o e-mail."""
        return self.__email

    def setNome(self, nome):
        """Altera o nome."""
        self.__nome = nome

    def setIdade(self, idade):
        """Altera a idade."""
        self.__idade = idade

    def setEmail(self, email):
        """Altera o e-mail."""
        self.__email = email
