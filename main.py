import random

from processo import Processo
from memoria import Memoria
from mmu import MMU

print("\nSIMULADOR DE MEMÓRIA VIRTUAL")
print("=" * 40)

print("\nConfiguração:")

print("Memória Principal: 64 KB")
print("Memória Virtual: 1 MB")
print("Frames: 8")
print("Páginas: 128")
print("Tamanho da página/frame: 8 KB")

memoria = Memoria()

mmu = MMU(memoria)

processo1 = Processo(1, 300000)
processo2 = Processo(2, 500000)

for i in range(20):

    processo = random.choice(
        [processo1, processo2]
    )

    endereco = random.randint(
        0,
        processo.tamanho - 1
    )

    mmu.acessar(
        processo,
        endereco
    )

    memoria.mostrar_memoria()

print("\nSimulação finalizada.")