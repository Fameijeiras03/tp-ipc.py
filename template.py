
############################# NO TOCAR ESTE CÓDIGO ############################
from random import randint
from time import time


def sacar_carta():
    '''
    Esta función toma una carta de un mazo de forma aleatoria. La carta está numerada del 1 al 10 (inclusive).

    params:
        Esta función no tiene parámetros de entrada.
    out:
        carta: int. El número de la carta sacada.
    '''
    carta = randint(1, 10)
    return carta
# variables
mazo = []
billetera = 500
apuesta = 0
mano_jugador = []
mano_crupier = []
i = 0
respuesta3 = "s"
respuesta4 = ""
respuesta5 = ""
respuestaFinal = ""
JugarDoble = ""

#Primer bucle para jugar todas las veces que se quiera

while respuestaFinal.lower() != "n":
    respuesta4 = ""
    respuesta3 = "s"
    respuesta1 = input('Quiere juegar? (s/n) ')
    if respuesta1.lower() == "s":           #Primer condicion a cumplirse, si se quiere jugar o no
        respuesta2 = input('Desea apostar?(s/n) ')
        if respuesta2.lower() == "s":           #Segunda condicion a cumplirse, si se quiere apostar
            mano_crupier.append(sacar_carta())          #Comienza el juego, se saca la primer carta del crupier
            print('El crupier a sacado un', mano_crupier[-1])           #Se muestra esa carta
            print(f"Usted tiene {billetera}")           #Muestra el dinero que tiene el jugador
            apuesta = input('Cuanto quiere apostar? ')          #Se le pregunta al jugador cuanto quiere apostar de ese dinero que tiene
            while billetera >= 0:           #Se comienza un bucle que contiene casi la totalidad del juego, solo si se tiene dinero
                if int(apuesta) <= billetera:           #Se contempla la apuesta realizada por el jugador, si es posible realizar en relacion al dinero que tiene
                    print('Empieza el juego')           #Si se puede realizar la apuesta, comienza el juego en si
                    while respuesta3.lower() == "s":        #Es un bucle que contempla la posibilidad de dejar de sacar cartas
                        if int(apuesta) > billetera:        #Condicional que verifica si el jugador puede jugar doble o nada
                            print("No posee suficiente dinero para jugar doble o nada")
                            break
                        mano_jugador.append(sacar_carta())          #Comienza a saccar cartas el jugador
                        print('Sus cartas son:', mano_jugador)          #Se van mostrando las cartas que va sacando el jugador
                        print('Usted tiene', sum(mano_jugador), "puntos")           #Se muestra la cantidad total de puntos que tiene el jugador
                        print(f'El crupier tiene un: {mano_crupier[0]}')
                        if sum(mano_jugador) <= 21:         #Si el jugador posee menos de 21 puntos totales, puede decidir si sigue sacando cartas
                            respuesta3 = input("Desea seguir jugando? (s/n) ")
                            continue
                        if sum(mano_jugador) > 21:          #Si el jugador posee mas de 21 puntos, automaticamente pierde
                            print("La partida termina, gana la banca")
                            billetera = billetera - int(apuesta)            #Se le descuenta la apuesta realizada
                            if billetera < 0:           #Si no tiene mas dinero en su billetera, lo expulsa del casino
                                print("No tiene mas dinero, vuelva en otro momento")
                                exit()
                            else:           #Si sigue teniendo dineron, le muestra cuanto de ese posee y si quiere apostar doble o nada
                                print(f"Le quedan {billetera}")
                                respuesta5 = input(
                                    "Quiere jugar a doble o nada? (s/n)")
                                mano_jugador.clear()            #Con este  codigo limpiamos la carta que saco el jugador
                                mano_crupier.clear()            #Con este  codigo limpiamos la carta que saco el crupier
                                if respuesta5.lower() == "s":       #Si quiere jugar doble o nada, se multiplica la apuesta y se comienza el bucle nuevamente
                                    int(apuesta)*2
                                    break
                                else:           #Si no quiere jugar doble o nada, se vuelve a la pregunta inicial
                                    respuesta4 = "n"
                                    break
                if respuesta3 == "n":           #En caso de que el jugador no quiera seguir sacando cartas, el crupier comienza a sacar sus cartas
                    while sum(mano_crupier) <= 16:          #El crupier saca cartas hasta que la suma total de estas da 16 o menos
                        mano_crupier.append(sacar_carta())
                        print(f"Las cartas del crupier son: {mano_crupier}")
                        print(f"El crupier suma {sum(mano_crupier)} puntos")
                    if sum(mano_crupier) > sum(mano_jugador) and sum(mano_crupier) <= 21:           #Si la suma de las cartas del crupier son mayores a las del jugador y menor a 21 puntos, el jugador pierde
                        print(f"Tus puntos son {sum(mano_jugador)}, y los de la mesa son {sum(mano_crupier)}")
                        print("La partida termina, gana la banca")          #Se repite lo de la perdida de jugador
                        billetera = billetera - int(apuesta)
                        if billetera < 0:
                            print("No tiene mas dinero, vuelva en otro momento")
                            exit()
                        else:
                            print(f"Le quedan {billetera}")
                            respuesta5 = input("Quiere jugar a doble o nada? (s/n)")
                            mano_jugador.clear()
                            mano_crupier.clear()
                            if respuesta5.lower() == "s":
                                int(apuesta)*2
                                break
                            else:
                                respuesta4 = "n"
                                break
                    if (sum(mano_crupier) < sum(mano_jugador)) or sum(mano_crupier) >= 22:          #Si la suma de las cartas del crupier son menores a las del jugador o la suma de sus cartas es mayor a 22, el jugador gana
                        print(f"Tus puntos son {sum(mano_jugador)}, y los de la mesa son {sum(mano_crupier)}")
                        print(f"La partida termino, has ganado {int(apuesta)}")
                        billetera = billetera + int(apuesta)            #Se le suma la puesta que habia hecho
                        print(f"Ahora tienes {billetera}")
                        mano_crupier.clear()
                        mano_jugador.clear()
                        respuesta4 = "n"
                        break
                if respuesta4.lower() == "n":
                    break
                if billetera <= 0:          #Si el jugador se queda sin dinero, lo hechan del casino
                    print("No tiene dinero, vuelva en otro momento")
                    exit()
                if int(apuesta) > billetera:            #Si la primer apuesta que realizo, es mayor a la cantidad de dinero que posee, le pide que realice otra apuesta
                    while int(apuesta) > billetera:
                        print(f'No tiene ese dinero, solo posee {billetera}')
                        apuesta = input('Ingrese otra apuesta ')
            if billetera <= 0:
                print("No tiene dinero, vuelva en otro momento")
                exit()
        if respuesta2 == "n":           #Es el mismo codigo pero sin apostar 
            print("Bueno, practiquemos")
            while respuesta3.lower() == "s":
                respuesta4 = ""
                mano_jugador.append(sacar_carta())
                print('Sus cartas son:', mano_jugador)
                print('Usted tiene', sum(mano_jugador), "puntos")
                if sum(mano_jugador) <= 21:
                    respuesta3 = input("Desea seguir jugando? (s/n) ")
                    continue
                if sum(mano_jugador) > 21:
                    print("La partida termina, gana la banca")
                    mano_jugador.clear()
                    mano_crupier.clear()
                    respuesta4 = input("Quiere volver a jugar? (s/n) ")
                    if respuesta4.lower() == "n":
                        break
                    else:
                        continue
            if respuesta3 == "n":
                while sum(mano_crupier) <= 16:
                    mano_crupier.append(sacar_carta())
                    print(f"Las cartas del crupier son: {mano_crupier}")
                    print(f"El crupier suma {sum(mano_crupier)} puntos")
                if sum(mano_crupier) > sum(mano_jugador) and sum(mano_crupier) <= 21:
                    print(f"Tus puntos son {sum(mano_jugador)}, y los de la mesa son {sum(mano_crupier)}")
                    print("La partida termina, gana la banca")
                    mano_jugador.clear()
                    mano_crupier.clear()
                    respuesta4 = input("Quiere volver a jugar? (s/n) ")
                    if respuesta4.lower() == "n":
                        break
                    else:
                        continue
                if (sum(mano_crupier) < sum(mano_jugador)) or sum(mano_crupier) >= 22:
                    print(f"Tus puntos son {sum(mano_jugador)}, y los de la mesa son {sum(mano_crupier)}")
                    mano_crupier.clear()
                    mano_jugador.clear()
                    respuesta4 = input("Quiere volver a jugar? (s/n) ")
                    if respuesta4.lower() == "n":
                        break
                    else:
                        continue
            if respuesta4.lower() == "n":
                break
    if respuesta1 == "n":           #Si no quiere jugar, lo despiden amablemente
        print("Lo esperamos la proxima")
        respuestaFinal = "n"
exit()
