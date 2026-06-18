# Trabalho 2 - Simulador de Memória Virtual

**Disciplina:** Análise e Aplicação de Sistemas Operacionais

## Objetivo

O objetivo deste trabalho é simular o funcionamento de um sistema de memória virtual com paginação, incluindo a tradução de endereços realizada pela MMU, gerenciamento da tabela de páginas, tratamento de faltas de página (Page Fault) e substituição de páginas utilizando o algoritmo FIFO.

## Configuração Utilizada

O simulador foi desenvolvido considerando as especificações fornecidas no enunciado:

* Memória Principal: 64 KB
* Memória Virtual: 1 MB
* Tamanho da Página: 8 KB
* Tamanho do Frame: 8 KB
* Total de Frames: 8
* Total de Páginas Virtuais: 128

## Técnica Escolhida

Para a implementação foi utilizada a abordagem **single-thread**.

Essa escolha foi feita para simplificar a visualização do fluxo de execução da MMU, permitindo observar de forma mais clara a tradução dos endereços, o carregamento de páginas e o algoritmo de substituição.

## Estrutura do Projeto

```text
trabalho_so/
├── main.py
├── memoria.py
├── mmu.py
├── processo.py
└── README.md
```

### processo.py

Responsável pela representação dos processos simulados.

Cada processo possui:

* PID (identificador)
* Tamanho do espaço de memória virtual

### memoria.py

Responsável pelo gerenciamento da memória principal.

Funções implementadas:

* Controle dos 8 frames disponíveis
* Verificação de frames livres
* Carregamento de páginas
* Substituição de páginas utilizando FIFO

### mmu.py

Implementa a MMU (Memory Management Unit).

Responsabilidades:

* Tradução de endereços virtuais para físicos
* Consulta da tabela de páginas
* Identificação de Page Fault
* Atualização da tabela de páginas

### main.py

Responsável pela execução da simulação.

Durante a execução:

* Dois processos são criados
* Endereços virtuais são gerados aleatoriamente
* A MMU realiza a tradução dos endereços
* A memória principal é atualizada
* Os resultados são exibidos no terminal

## Funcionamento

Quando um processo solicita acesso a um endereço virtual:

1. A MMU calcula a página e o offset.
2. A tabela de páginas é consultada.
3. Caso a página esteja carregada:

   * O endereço físico é calculado.
4. Caso a página não esteja carregada:

   * Ocorre um Page Fault.
   * A página é carregada para a memória principal.
   * A tabela de páginas é atualizada.
5. Se não houver frames livres:

   * O algoritmo FIFO escolhe uma página para remoção.
   * A nova página é carregada.

## Algoritmo FIFO

Foi utilizado o algoritmo FIFO (First In First Out) para substituição de páginas.

A página carregada há mais tempo na memória principal é a primeira a ser removida quando não existem frames livres.

Exemplo:

```text
PAGE FAULT
FIFO removeu página (2, 36)
Página carregada no frame 0
```

## Exemplo de Saída

```text
Processo: 2
Endereço virtual: 302224
Página: 36
Offset: 7312

PAGE FAULT

Página carregada no frame 0

Endereço físico: 7312
```

## Como Executar

No terminal:

```bash
python3 main.py
```

## Conceitos Aplicados

* Memória Virtual
* Memória Principal
* Paginação
* Frames
* Tabela de Páginas
* MMU
* Tradução de Endereços
* Page Fault
* Algoritmo FIFO
* Gerenciamento de Memória

## Autor

Luiz Felipe Hilgert

Curso de Ciência da Computação – Unisinos
