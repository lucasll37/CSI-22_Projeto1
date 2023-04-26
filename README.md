# CSI-22_Projeto1

python >= 3.7.0

git

#### Estrutura de Diretório
```
└─── ASSETS: artes de cenário, objetos e personagens
└─── SOUNDS: efeito sonores e músicas
└─── SRC:
      └─── : MAIN.PY: Arquivo de entrada
      └─── : GAME: Classe do Jogo
      └─── : OBJ.PY: Classe de objetos
      └─── : SCENEN: Classe de Cenas do Jogo
      └─── : PLANE.PY Classe avião (herda Obj)
      └─── : PLAYER.PY Classe jogador (herda Obj)
      └─── : WINDOW.PY Classe Janela (Gráfica)

```

#### Overview do Projeto
  Este projeto é um game desenvolvido com a linguagem de Programação Python, com o auxilio da biblioteca Pygame.

  O paradigma de Programação empregado foi Programação Orientada à Objeto (POO).

A execução da aplicação se inicia pelo arquivo `main.py`. Nele é instanciado um objeto da classe game. Por sua vez, a instancia de game instancia uma janela de execução (classe Window) e as cenas do jogo.

Todo objeto, herda direta ou inderetamente da classe Obj, que implementa efeitos de transição de imagens para dar o efeito de movimento mais realista dentre outras funcionalidades.

Com excessão das cenas de fechamento (vitória e derrota) que são condiconais, todas as demais cenas são isoladas em módulos python e autocontidas. Uma vez sendo passada para o objeto de classe Window em sua inicialização, esse proprio objeto se responsabiliza por percorrer as cenas segundo a ordem com que foram transmitidas inicialmente, executando seus métodos de updates, events, e impressão em tela dos elementos que compõem o cenário. 

#### Com o terminal no diretório raiz do projeto, siga os passos:

- Prefenciamente em um ambiente isolado do python, execute:

  `pip install -r requirements`


- Para executar o jogo, abra o terminal na pasta raiz do diretório e execute: `python ./src/main.py` ou comando análogo (a depender do SO).

#### Os comando e enredo do jogo são apresentados ao longo do mesmo. A interação se dá unicamente através do seu teclado.

## Boa diversão!!! :)