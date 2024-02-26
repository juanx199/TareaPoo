from blackjack import * 

class Juego:
    def __init__(self):
        self.mazo = Mazo()
        self.casa = Mazo(True)
        self.jugador = Mazo(True)

    def iniciar_juego(self):
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())

    def mostrar_juego_jug(self,mostrar=True):
        print("\n Mazo jugador: ")
        self.jugador.mostrar_cartas(mostrar)
    
    def mostrar_juego_cas(self,mostrar=False):
        print("\n Mazo casa: ")
        if mostrar:
            self.casa.mostrar_cartas(True)
        else:
            self.casa.mostrar_cartas()
            
    def mostrar_todas_cartas(self):
        print("\n Mazo jugador: ")
        self.jugador.mostrar_cartas(True)
        