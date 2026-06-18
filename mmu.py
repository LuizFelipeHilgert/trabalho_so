PAGE_SIZE = 8192  

class MMU:
    def __init__(self, memoria):
        self.memoria = memoria
        self.tabela_paginas = {}

    def acessar(self, processo, endereco_virtual):
        pagina = endereco_virtual // PAGE_SIZE
        offset  = endereco_virtual % PAGE_SIZE

        print("\n" + "=" * 50)
        print(f"  Processo : {processo.pid}")
        print(f"  Endereço virtual : {endereco_virtual} (0x{endereco_virtual:05X})")
        print(f"  Página           : {pagina}")
        print(f"  Offset           : {offset}")

        chave = (processo.pid, pagina)

        if chave in self.tabela_paginas:
            frame = self.tabela_paginas[chave]
            print(f"  Status           : HIT — página encontrada na RAM")
            print(f"  Frame            : {frame}")
        else:
            print(f"  Status           : PAGE FAULT — página ausente na RAM")

            inicio = pagina * PAGE_SIZE
            fim    = min(inicio + PAGE_SIZE, len(processo.memoria_virtual))
            dados_pagina = bytearray(processo.memoria_virtual[inicio:fim])
            if len(dados_pagina) < PAGE_SIZE:
                dados_pagina += bytearray(PAGE_SIZE - len(dados_pagina))

            frame, removida = self.memoria.carregar_pagina(chave, dados_pagina)

            if removida is not None:
                pid_rem, pag_rem = removida
                print(f"  FIFO removeu     : Processo {pid_rem} | Página {pag_rem} (Frame {frame})")
                if removida in self.tabela_paginas:
                    del self.tabela_paginas[removida]

            self.tabela_paginas[chave] = frame
            print(f"  Página carregada : Frame {frame}")

        frame = self.tabela_paginas[chave]
        endereco_fisico = frame * PAGE_SIZE + offset
        dado = self.memoria.ler_dado(frame, offset)

        print(f"  Endereço físico  : {endereco_fisico} (0x{endereco_fisico:05X})")
        print(f"  Conteúdo acessado: {dado} (0x{dado:02X})")

        return endereco_fisico