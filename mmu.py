PAGE_SIZE = 8192

class MMU:

    def __init__(self, memoria):

        self.memoria = memoria

        self.tabela_paginas = {}

    def acessar(self, processo, endereco_virtual):

        pagina = endereco_virtual // PAGE_SIZE

        offset = endereco_virtual % PAGE_SIZE

        print("\n----------------------------------")
        print(f"Processo: {processo.pid}")
        print(f"Endereço virtual: {endereco_virtual}")
        print(f"Página: {pagina}")
        print(f"Offset: {offset}")

        chave = (processo.pid, pagina)

        if chave in self.tabela_paginas:

            frame = self.tabela_paginas[chave]

            print("Página encontrada na memória.")

        else:

            print("PAGE FAULT")

            frame, removida = self.memoria.carregar_pagina(
                chave
            )

            if removida is not None:

                print(
                    f"FIFO removeu página {removida}"
                )

                del self.tabela_paginas[removida]

            self.tabela_paginas[chave] = frame

            print(
                f"Página carregada no frame {frame}"
            )

        endereco_fisico = frame * PAGE_SIZE + offset

        print(f"Endereço físico: {endereco_fisico}")

        return endereco_fisico