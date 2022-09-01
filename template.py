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
    carta = randint(1,10)
    return carta
######################## EJEMPLO DE USO DE SACAR_CARTA ########################
#c = sacar_carta()
#print(c)
#En la consola se vería:    8

########################### AQUÍ COMIENZA TU CÓDGIO ###########################
#variables 
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
    if respuesta1.lower() == "s" :
        respuesta2 = input('Desea apostar?(s/n) ')
        if respuesta2.lower() == "s" :
            mano_crupier.append( sacar_carta())
            print('El crupier a sacado un' ,mano_crupier[-1])
            print(f"Usted tiene {billetera}")
            apuesta = input('Cuanto quiere apostar? ')
            while billetera >= 0:
                if int(apuesta) > billetera:
                    while int(apuesta) > billetera:
                        print(f'No tiene ese dinero, solo posee {billetera}')  #deberia ir un while
                        apuesta = input('Ingrese otra apuesta ')
                        if int(apuesta) < billetera:
                            break
                        else:
                            continue
                if int(apuesta) <= billetera:
                    billetera = billetera - int(apuesta)
                    print('Empieza el juego')
                    while respuesta3.lower() == "s":
                        mano_jugador.append( sacar_carta())
                        print('Su carta es un:', mano_jugador[-1])
                        print('Hasta ahora tiene' , sum(mano_jugador) , "puntos")
                        if sum(mano_jugador) <= 21:
                            respuesta3 = input("Desea seguir jugando? (s/n) ")
                            continue
                        if sum(mano_jugador) > 21:
                            print("La partida termina, gana la banca")
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
                if respuesta3 == "n":
                    while sum(mano_crupier) <= 16:
                        mano_crupier.append(sacar_carta())
                        print(f"El crupier a sacado un: {mano_crupier[-1]}")
                        print(f"hasta ahora el crupier tiene {sum(mano_crupier)}")
                    if sum(mano_crupier) > sum(mano_jugador) and sum(mano_crupier) <= 21:
                        print(f"Tus puntos son {sum(mano_jugador)}, y los de la mesa son {sum(mano_crupier)}")
                        print("La partida termina, gana la banca")
                        print(f"Ahora tienes {billetera}")
                        respuesta5 = input("Quiere jugar a doble o nada? (s/n)")
                        mano_crupier.clear()
                        mano_jugador.clear()
                        if respuesta5.lower() == "s":
                            int(apuesta)*2

                            continue
                        else:
                            respuesta4 = "n"
                            break
                    if (sum(mano_crupier) < sum(mano_jugador) and sum(mano_crupier) <= 21) or sum(mano_crupier)>= 22 :
                        print(f"Tus puntos son {sum(mano_jugador)}, y los de la mesa son {sum(mano_crupier)}")
                        print(f"La partida termino, has ganado {int(apuesta)}")
                        billetera = billetera + int(apuesta)*2
                        print(f"Ahora tienes {billetera}")
                        mano_crupier.clear()
                        mano_jugador.clear()
                        break
                if respuesta4.lower() == "n":
                    break
        if respuesta2 == "n":
            print("Bueno, pratiquemos entonces")
            while respuesta2.lower() == "n":
                print('Empieza el juego')
                while respuesta3.lower() == "s":
                    mano_jugador.append( sacar_carta())
                    print('Su carta es un:', mano_jugador[-1])
                    print('Hasta ahora tiene' , sum(mano_jugador) , "puntos")
                    if sum(mano_jugador) <= 21:
                        respuesta3 = input("Desea seguir jugando (s/n) ")
                        continue
                    if sum(mano_jugador) > 21:
                        print("La partida termina, gana la banca")
                        respuesta4 = input("Quiere seguir jugando? (s/n) ")
                        mano_jugador.clear()
                        mano_crupier.clear()
                        if respuesta4.lower() == "s":
                            continue
                        else:
                            break
                if respuesta3.lower == "n":
                    while sum(mano_crupier) <= 16:
                            mano_crupier.append(sacar_carta())
                    if sum(mano_crupier) > sum(mano_jugador) and sum(mano_crupier) <= 21:
                            print(f"Tus puntos son {sum(mano_jugador)}, y los de la mesa son {sum(mano_crupier)}")
                            print("la partida termina, gana la banca")
                            mano_crupier.clear()
                            mano_jugador.clear()
                            respuesta4 = "n"
                            break
                    if sum(mano_crupier) < sum(mano_jugador) and sum(mano_crupier) <= 21:
                            print(f"Tus puntos son {sum(mano_jugador)}, y los de la mesa son {sum(mano_crupier)}")
                            print("la partida termino, has ganado")
                            mano_jugador.clear()
                            mano_crupier.clear()
                            break
                if respuesta4.lower() == "n":
                        break
            if billetera < 0:
                print(f"No le queda mas dinero, usted nos debe {billetera}, larguese de aqui")
                exit()
    if respuesta1 == "n":
        print(f"Se queda con {billetera}")
        print("Lo esperamos la proxima")
        respuestaFinal = "n"

