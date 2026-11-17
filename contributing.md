# Contribuindo

## Antes de enviar uma alteração

1. Execute o programa: python cadastro/src/main.py
2. Confira as mudanças: git status e git diff
3. Execute as análises: python -m pylint --rcfile=.pylintrc cadastro/src e python -m radon cc cadastro/src -s
4. Faça um commit com uma mensagem objetiva.

## Convenções

- Um commit representa uma alteração verificável.
- Não inclua dados reais de pessoas no repositório.
- Registre decisões e resultados relevantes no histórico Git.
- Arquivos gerados (como `__pycache__/` e `*.pyc`) não são versionados: podem ser recriados a qualquer momento pela execução do programa e só poluem o histórico e os diffs. Por isso estão no `.gitignore`.

## Padrões de código

- nomes claros e consistentes
- funções e variáveis em snake_case; classes em PascalCase; métodos em camelCase (get/set de `Pessoa`)
- evitar duplicação
- responsabilidade identificável
- tratar entradas inválidas

## Decisões sobre o Pylint

- Mantidas: C0103 (nomes), W0612 (variável não usada), W0621 (nome redefinido), pelos problemas de manutenção e clareza que causam.
- Ajustado: max-line-length = 100, para ficar legível nas telas e exemplos da disciplina.
- Ajustado: method-naming-style = camelCase, porque os métodos de `Pessoa` e `CadastroPessoas` seguem o padrão getNome/setNome/buscarPorNome adotado na disciplina.
- Desabilitadas temporariamente: C0114 e C0116 (docstrings). Revisar quando a estrutura do projeto estabilizar.

## Antes de iniciar

Certifique-se de que está trabalhando com a versão atualizada do projeto:

git switch main
git pull
git status
