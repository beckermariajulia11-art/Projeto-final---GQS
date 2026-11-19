from pessoa import Pessoa # pylint: disable=import-error


def test_alterar_idade():
    # PREPARAR
    pessoa = Pessoa("Ana", 20, "ana@example.com")

    # EXECUTAR
    pessoa.setIdade(21)

    # VERIFICAR
    assert pessoa.getIdade() == 21
