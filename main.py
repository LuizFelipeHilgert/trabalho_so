import random
from processo import Processo
from memoria import Memoria
from mmu import MMU

print("\n" + "#" * 50)
print("  SIMULADOR DE MEMÓRIA VIRTUAL")
print("#" * 50)
print("\n  Configuração do sistema:")
print("  - Memória Principal  : 64 KB (8 frames de 8 KB)")
print("  - Memória Virtual    : 1 MB (128 páginas de 8 KB)")
print("  - Algoritmo de sub.  : FIFO")

tamanho1 = random.randint(1, 1024 * 1024)
tamanho2 = random.randint(1, 1024 * 1024)

processo1 = Processo(1, tamanho1)
processo2 = Processo(2, tamanho2)

print(f"\n  Processo 1: {tamanho1} bytes")
print(f"  Processo 2: {tamanho2} bytes")

memoria = Memoria()
mmu = MMU(memoria)

NUM_INSTRUCOES = 20

print(f"\n  Iniciando simulação com {NUM_INSTRUCOES} instruções...\n")

for i in range(NUM_INSTRUCOES):
    print(f"\n>>> Instrução {i + 1}")
    processo = random.choice([processo1, processo2])
    endereco = random.randint(0, processo.tamanho - 1)
    mmu.acessar(processo, endereco)
    memoria.mostrar_memoria()

print("\n" + "#" * 50)
print("  Simulação finalizada.")
print("#" * 50)