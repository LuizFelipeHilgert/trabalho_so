from collections import deque

class Memoria:

    def __init__(self):

        self.frames = [None] * 8

        self.fifo = deque()

    def frame_livre(self):

        for i in range(len(self.frames)):
            if self.frames[i] is None:
                return i

        return -1

    def carregar_pagina(self, pagina):

        livre = self.frame_livre()

        if livre != -1:

            self.frames[livre] = pagina

            self.fifo.append(pagina)

            return livre, None

        pagina_removida = self.fifo.popleft()

        frame = self.frames.index(pagina_removida)

        self.frames[frame] = pagina

        self.fifo.append(pagina)

        return frame, pagina_removida

    def mostrar_memoria(self):

        print("\nFrames ocupados:")

        for i, pagina in enumerate(self.frames):
            print(f"Frame {i}: {pagina}")