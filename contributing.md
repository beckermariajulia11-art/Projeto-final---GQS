# Contribuindo com o projeto

## Padrões de código

- nomes claros e consistentes
- funções e variáveis em snake_case
- evitar duplicação
- responsabilidade identificável
- tratar entradas inválidas

## Verificações

- executar o programa
- executar o Pylint
- corrigir ou justificar
- realizar o commit

## Ferramentas

Pylint · pre-commit · Git

## Decisões sobre o Pylint

- Mantidas: C0103 (nomes), W0612 (variável não usada), W0621 (nome redefinido), pelos problemas de manutenção e clareza que causam.
- Ajustado: max-line-length = 100, para ficar legível nas telas e exemplos da disciplina.
- Desabilitadas temporariamente: C0114 e C0116 (docstrings). O módulo ainda está evoluindo; revisar quando a estrutura do projeto estabilizar.
- Mantido no código: too-many-branches em `analisar_pessoa`, até a refatoração planejada.