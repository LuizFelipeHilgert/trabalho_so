# Trabalho 2 - Simulador de Memória Virtual

**Disciplina:** Análise e Aplicação de Sistemas Operacionais

## Objetivo

O objetivo deste trabalho é simular o funcionamento de um sistema de memória virtual com paginação, incluindo a tradução de endereços realizada pela MMU, gerenciamento da tabela de páginas, tratamento de faltas de página (Page Fault) e substituição de páginas utilizando o algoritmo FIFO.

## Configuração Utilizada

O simulador foi desenvolvido considerando as especificações fornecidas no enunciado:

- Memória Principal: 64 KB
- Memória Virtual: 1 MB
- Tamanho da Página: 8 KB
- Tamanho do Frame: 8 KB
- Total de Frames: 8
- Total de Páginas Virtuais: 128

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

- PID (identificador)
- Tamanho do espaço de memória virtual (aleatório entre 1 byte e 1 MB)
- Memória virtual com dados reais (`bytearray` de bytes aleatórios), simulando o conteúdo que o processo armazena em seu espaço de endereçamento virtual

### memoria.py

Responsável pelo gerenciamento da memória principal.

Funções implementadas:

- Controle dos 8 frames disponíveis
- Armazenamento dos dados reais de cada página carregada nos frames
- Verificação de frames livres
- Carregamento de páginas (copia o bloco de dados da memória virtual para o frame)
- Substituição de páginas utilizando FIFO
- Leitura do conteúdo de um byte específico a partir de frame e offset

### mmu.py

Implementa a MMU (Memory Management Unit).

Responsabilidades:

- Tradução de endereços virtuais para físicos
- Consulta da tabela de páginas
- Identificação de Page Fault
- Atualização da tabela de páginas após carregamento
- Exibição do conteúdo do processo no endereço acessado (em ambos os casos: HIT e PAGE FAULT)

### main.py

Responsável pela execução da simulação.

Durante a execução:

- Dois processos são criados com tamanhos aleatórios entre 1 byte e 1 MB
- Endereços virtuais são gerados aleatoriamente dentro do espaço de cada processo
- A MMU realiza a tradução dos endereços
- A memória principal é atualizada
- Os resultados são exibidos no terminal

## Funcionamento

Quando um processo solicita acesso a um endereço virtual:

1. A MMU calcula o número de página e o offset a partir do endereço virtual.
2. A tabela de páginas é consultada.
3. Caso a página esteja carregada (HIT):
   - O endereço físico é calculado.
   - O conteúdo do processo naquele endereço é exibido.
4. Caso a página não esteja carregada (PAGE FAULT):
   - Um PAGE FAULT é emitido na saída padrão.
   - O bloco de dados correspondente é copiado da memória virtual para a memória principal.
   - A tabela de páginas é atualizada.
   - O endereço físico é calculado e o conteúdo do processo naquele endereço é exibido.
5. Se não houver frames livres durante o carregamento:
   - O algoritmo FIFO escolhe uma página para remoção.
   - A nova página é carregada no frame liberado.

## Algoritmo FIFO

Foi utilizado o algoritmo FIFO (First In First Out) para substituição de páginas.

A página carregada há mais tempo na memória principal é a primeira a ser removida quando não existem frames livres.

Exemplo:

```text
Status           : PAGE FAULT — página ausente na RAM
FIFO removeu     : Processo 2 | Página 36 (Frame 0)
Página carregada : Frame 0
```

## Exemplo de Saída

```text
>>> Instrução 1

==================================================
  Processo : 2
  Endereço virtual : 302224 (0x49CD0)
  Página           : 36
  Offset           : 7312
  Status           : PAGE FAULT — página ausente na RAM
  Página carregada : Frame 0
  Endereço físico  : 7312 (0x01C90)
  Conteúdo acessado: 218 (0xDA)

  Estado da Memória Principal (RAM):
  ------------------------------------
  Frame 0: Processo 2 | Página 36
  Frame 1: [livre]
  Frame 2: [livre]
  Frame 3: [livre]
  Frame 4: [livre]
  Frame 5: [livre]
  Frame 6: [livre]
  Frame 7: [livre]
  ------------------------------------

>>> Instrução 2

==================================================
  Processo : 2
  Endereço virtual : 300000 (0x493E0)
  Página           : 36
  Offset           : 5088
  Status           : HIT — página encontrada na RAM
  Frame            : 0
  Endereço físico  : 5088 (0x013E0)
  Conteúdo acessado: 105 (0x69)
```

## Como Executar

No terminal:

```bash
python3 main.py
```

## Conceitos Aplicados

- Memória Virtual
- Memória Principal
- Paginação
- Frames
- Tabela de Páginas
- MMU
- Tradução de Endereços
- Page Fault
- Algoritmo FIFO
- Gerenciamento de Memória

----------------------------------
Curso de Ciência da Computação – Unisinos