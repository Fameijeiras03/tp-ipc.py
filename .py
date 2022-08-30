 if int(apuesta) > billetera:
            print('No tiene ese dinero')  #deberia ir un while
            print('Ingrese otra apuesta')
>>>>>>> 5fcf9b577cd20885e712b1b05e2fba80b3e5aac2
            apuesta = input('Cuanto quiere apostar? ')
            while int(apuesta) > billetera :
                apuesta = input('No cuenta con ese dinero, ingrese otra apuesta: ')
            if int(apuesta) <= billetera:
                        billetera = billetera - int(apuesta)
                        print('Empieza el juego')
                        mano_jugador.append( sacar_carta())
                        print('Su primera carta es un:', mano_jugador)
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