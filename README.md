# CSI-22_Projeto1

python >= 3.7.0

git

#### Com o terminal no diretório raiz do projeto, siga os passos:

- Prefenciamente em um ambiente isolado do python, execute:

  `pip install -r requirements`

#### No presente momento, a pasta contém um exemplo de jogo. A pasta `example_procedural` é uma versão implementada "à moda" C. Já a pasta `example_poo`, aos moldes da programação orientada a objetos.

Para executar qualquer uma das versões, abra o terminal na pasta raiz do diretório desejado e execute `python ./src/main.py` ou comando análogo (a depender do SO).

## Dicas de uso do Git/Github

- Clone o repositório:
  `git clone <link>`
- Periodicamente, após alterar o código, faça upload do código:

  ```
  git status
  git pull
  git add .
  git commit -am "<comentário obrigatório>"
  git push
  ```

O comando `git pull` atualiza o seu códido local (em relação ao código remoto), fazendo você tratar as divergências localmente, caso existam, antes de submetê-lo ao github.
