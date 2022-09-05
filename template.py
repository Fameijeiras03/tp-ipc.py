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
######################## EJEMPLO DE USO DE SACAR_CARTA ########################
#c = sacar_carta()
# print(c)
# En la consola se vería:    8


########################### AQUÍ COMIENZA TU CÓDGIO ###########################
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

while respuestaFinal.lower() != "n":
    respuesta4 = ""
    respuesta3 = "s"
    respuesta1 = input('Quiere juegar? (s/n) ')
    if respuesta1.lower() == "s":
        respuesta2 = input('Desea apostar?(s/n) ')
        if respuesta2.lower() == "s":
            mano_crupier.append(sacar_carta())
            print('El crupier a sacado un', mano_crupier[-1])
            print(f"Usted tiene {billetera}")
            apuesta = input('Cuanto quiere apostar? ')
            while billetera >= 0:
                if int(apuesta) <= billetera:
                    print('Empieza el juego')                    
                    while respuesta3.lower() == "s":
                        if int(apuesta) > billetera:
                            print(
                                "No posee suficiente dinero para jugar doble o nada")
                            break
                        mano_jugador.append(sacar_carta())
                        print('Sus cartas son:', mano_jugador)
                        print('Usted tiene', sum(mano_jugador), "puntos")
                        if sum(mano_jugador) <= 21:
                            respuesta3 = input("Desea seguir jugando? (s/n) ")
                            continue
                        if sum(mano_jugador) > 21:
                            print("La partida termina, gana la banca")
                            billetera = billetera - int(apuesta)
                            if billetera < 0:
                                print("No tiene mas dinero, vuelva en otro momento")
                                exit()
                            else:
                                print(f"Le quedan {billetera}")
                                respuesta5 = input(
                                    "Quiere jugar a doble o nada? (s/n)")
                                mano_jugador.clear()
                                mano_crupier.clear()
                                if respuesta5.lower() == "s":
                                    int(apuesta)*2
                                    continue
                                else:
                                    respuesta4 = "n"
                                    break
                if respuesta3 == "n":
                    while sum(mano_crupier) <= 16:
                        mano_crupier.append(sacar_carta())
                        print(f"Las cartas del crupier son: {mano_crupier}")
                        print(f"El crupier suma {sum(mano_crupier)} puntos")
                    if sum(mano_crupier) > sum(mano_jugador) and sum(mano_crupier) <= 21:
                        print(f"Tus puntos son {sum(mano_jugador)}, y los de la mesa son {sum(mano_crupier)}")
                        print("La partida termina, gana la banca")
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
                                continue
                            else:
                                respuesta4 = "n"
                                break
                    if (sum(mano_crupier) < sum(mano_jugador)) or sum(mano_crupier) >= 22:
                        print(
                            f"Tus puntos son {sum(mano_jugador)}, y los de la mesa son {sum(mano_crupier)}")
                        print(f"La partida termino, has ganado {int(apuesta)}")
                        billetera = billetera + int(apuesta)
                        print(f"Ahora tienes {billetera}")
                        mano_crupier.clear()
                        mano_jugador.clear()
                        break
                if respuesta4.lower() == "n":
                    break
                if int(apuesta) > billetera:
                    while int(apuesta) > billetera:
                        print(f'No tiene ese dinero, solo posee {billetera}')
                        apuesta = input('Ingrese otra apuesta ')
            if billetera < 0:
                print("No tiene dinero, vuelva en otro momento")
                exit()
        if respuesta2 == "n":
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
                    print(
                        f"Tus puntos son {sum(mano_jugador)}, y los de la mesa son {sum(mano_crupier)}")
                    print(f"La partida termino, has ganado {int(apuesta)}")
                    mano_crupier.clear()
                    mano_jugador.clear()
                    respuesta4 = input("Quiere volver a jugar? (s/n) ")
                    if respuesta4.lower() == "n":
                        break
                    else:
                        continue
            if respuesta4.lower() == "n":
                break
    if respuesta1 == "n":
        print("Lo esperamos la proxima")
        respuestaFinal = "n"
exit()
