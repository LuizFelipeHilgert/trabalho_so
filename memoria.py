from collections import deque

PAGE_SIZE = 8192  

class Memoria:
    def __init__(self):
        self.frames = [None] * 8         
        self.dados_frames = [None] * 8    
        self.fifo = deque()             

    def frame_livre(self):
        for i, f in enumerate(self.frames):
            if f is None:
                return i
        return -1

    def carregar_pagina(self, chave_pagina, dados_pagina):
        """
        Carrega uma página na memória principal.
        chave_pagina: tupla (pid, numero_pagina)
        dados_pagina: bytearray com os bytes dessa página extraídos da memória virtual

        Retorna: (frame_index, pagina_removida_ou_None)
        """
        livre = self.frame_livre()

        if livre != -1:
            self.frames[livre] = chave_pagina
            self.dados_frames[livre] = dados_pagina
            self.fifo.append(livre)
            return livre, None

        frame_vitima = self.fifo.popleft()
        pagina_removida = self.frames[frame_vitima]

        self.frames[frame_vitima] = chave_pagina
        self.dados_frames[frame_vitima] = dados_pagina
        self.fifo.append(frame_vitima)

        return frame_vitima, pagina_removida

    def ler_dado(self, frame_index, offset):
        """Retorna o byte no offset dentro do frame informado."""
        if self.dados_frames[frame_index] is None:
            return None
        return self.dados_frames[frame_index][offset]

    def mostrar_memoria(self):
        print("\n  Estado da Memória Principal (RAM):")
        print("  " + "-" * 36)
        for i, pagina in enumerate(self.frames):
            if pagina is None:
                print(f"  Frame {i}: [livre]")
            else:
                pid, num_pag = pagina
                print(f"  Frame {i}: Processo {pid} | Página {num_pag}")
        print("  " + "-" * 36)