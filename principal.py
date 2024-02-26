from juego import *
 
print("\t   BIENVENIDO\n \tVAMOS A JUGAR 21 \n") 
 
juego = Juego()
juego.iniciar_juego()
juego.mostrar_juego_jug(False)
juego.mostrar_juego_cas(False)

while juego.jugador.dar_valor()<= 21:
    opcion = int(input("Si deseas añadir otra carta presiona 1 \nSi deseas plantarte presiona 2 \n"))
    
    if opcion == 1:
        juego.jugador.agregar_carta(juego.mazo.dar_carta())
        juego.mostrar_juego_jug()
        print("Tu puntaje es: ")
        print( juego.jugador.dar_valor())
        juego.mostrar_juego_cas()
    else:    
        print("La casa sigue jugando")
        while juego.casa.dar_valor()<17:
            juego.casa.agregar_carta(juego.mazo.dar_carta())
            juego.mostrar_juego_cas()
            print("Puntaje casa: ")
            print(juego.casa.dar_valor())
        break
if juego.jugador.dar_valor() > juego.casa.dar_valor() and juego.jugador.dar_valor()<= 21 and juego.casa.dar_valor()<=21:
    print(juego.mostrar_juego_jug())
    print("¡EL JUGADOR HA GANADO!\nTu puntaje es: ")
    print(juego.jugador.dar_valor())
    
elif juego.casa.dar_valor() > juego.jugador.dar_valor() and juego.casa.dar_valor()<=21 and juego.jugador.dar_valor()<= 21:
   
    print("!LA CASA HA GANADO¡\n Puntaje casa:")
    print(juego.casa.dar_valor())
    
elif juego.jugador.dar_valor() >21:
    print(juego.mostrar_juego_jug())
    print("¡EL JUGADOR HA PERDIDO ;C¡\n Tu puntaje es:")
    print( juego.jugador.dar_valor())
    
elif juego.casa.dar_valor() >21:
   
    print("¡LA CASA HA PERDIDO!\n Puntaje casa: ")
    print(juego.casa.dar_valor())    
    
else:
    print(juego.mostrar_juego_jug())
    print("¡HA HABIDO UN EMPATEE! LA CASA GANA\n Tu puntaje es: \n")
    print( juego.jugador.dar_valor())
    print(juego.mostrar_juego_cas())
    print("Puntaje casa: ")
    print(juego.casa.dar_valor())         
    
#Hacer la comparación de puntajes

#Dar el mensaje de quién gano
#Preguntar si se desea jugar nuevamente
