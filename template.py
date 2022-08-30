############################# NO TOCAR ESTE CÓDIGO ############################
from random import randint



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
respuesta3 = "si"

mano_crupier.append( sacar_carta())
print('El crupier a sacado un' ,mano_crupier[-1])
respuesta1 = input('Quiere juegar? ')

if respuesta1.lower() == 'si' : # .lower() --> sin importar como ingrese la respuesta, se convierte a lowercase
    respuesta2 = input('Desea apostar? ')
    if respuesta2.lower() == 'si' :
        apuesta = input('Cuanto quiere apostar? ')  
        if int(apuesta) <= billetera:
            billetera = billetera - int(apuesta)
            print('Empieza el juego')
            while respuesta3.lower() == "si":
                mano_jugador.append( sacar_carta())
                print('Su carta es un:', mano_jugador[-1])
                print('Hasta ahora tiene' , sum(mano_jugador) , "puntos")
                if sum(mano_jugador) <= 21:
                    respuesta3 = input("Desea seguir jugando ")
                    continue
                if sum(mano_jugador) > 21:
                    print("Perdiste")
                break
                
                
        if int(apuesta) > billetera:
            print('No tiene ese dinero')  #deberia ir un while
            print('Ingrese otra apuesta')
            apuesta = input('Cuanto quiere apostar? ')
            
    #if respuesta2.lower() == 'no' :
        
       




#while(): # Repetición del juego
    #Tu código va acá
    #while(): # Turno del jugador
        #Tu código va acá
    #while(): # Turno del crupier
    	#Tu código va acá