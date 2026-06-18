import random

class Processo:
    def __init__(self, pid, tamanho):
        self.pid = pid
        self.tamanho = tamanho
        self.memoria_virtual = bytearray(
            random.randint(0, 255) for _ in range(tamanho)
        )

    def __repr__(self):
        return f"Processo(pid={self.pid}, tamanho={self.tamanho} bytes)"