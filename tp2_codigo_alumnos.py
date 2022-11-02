""" >>>> NO TOCAR ESTE CÓDIGO >>>> """

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def str2datetime(date, fmt="%Y-%m-%d"):
    """Convierte una cadena (o secuencia de cadenas) a tipo datetime (o secuencia de datetimes).

    ENTRADAS:
        date (str ó secuencia de str): fechas a convertir.
        fmt (str, opcional): formato de fecha (ver documentación de biblioteca datetime).
    SALIDAS:
        output (datetime ó secuencia de datetime): fechas convertidas a datetime.
    EJEMPLOS:
    >>>> date = str2datetime('2022-10-24')
    >>>> print(date.year, date.month, date.day)

    >>>> date = str2datetime(['2022-10-24', '2022-10-23', '2022-10-22'])
    >>>> print(len(date))"""
    if isinstance(date, str):
        return datetime.strptime(date, fmt)
    elif isinstance(date, (list, np.ndarray)):
        output = []
        for d in date:
            output.append(datetime.strptime(d, fmt))
        if isinstance(date, np.ndarray):
            output = np.array(output)
        return output


def datetime2str(date, fmt="%Y-%m-%d"):
    """Convierte un datetime (o secuencia de datetimes) a tipo str (o secuencia de str).

    ENTRADAS:
        date (datetime ó secuencia de datetime): fechas a convertir.
        fmt (str, opcional): formato de fecha (ver documentación de biblioteca datetime).
    SALIDAS:
        output (str ó secuencia de str): fechas convertidas a cadenas.
    EJEMPLOS:
    >>>> date_str = '2022-10-24'
    >>>> date = str2datetime(date_str)
    >>>> print(datetime2str(date) == date_str)"""
    if isinstance(date, datetime):
        return date.strftime(fmt)
    elif isinstance(date, (list, np.ndarray)):
        output = []
        for d in date:
            output.append(d.strftime(fmt))
        if isinstance(date, np.ndarray):
            output = np.array(output)
        return output


""" >>>> DEFINAN SUS FUNCIONES A PARTIR DE AQUÍ >>>> """

FILE_NAME = "C:\\Users\\franc\\OneDrive\\Desktop\\UDESA\\IPC\\Guia-de-ejercicios\\tp2\\bolsa.csv"

def read_file (file_name):
    """
    Lee un archivo csv y devuelve un diccionario donde las claves 
    son los nombres de las columnas y los valores son las filas del archivo csv
    
    Entrada:  
        Un archivo csv
    Salida: 
        Un diccionario con el nombre de las columnas como claves y los valores como listas.
    """
    dicc = {}
    f = open(file_name)
    for i, row  in enumerate(f):
        row = row.strip('\n')
        if i == 0:
            lista1 = row.split(',')
            for x in lista1:
                dicc[x] = []
        if i !=0:
            lista2 = row.split(',')
            for indice, y in enumerate(lista2):
            
                if indice != 0:
                    y = float(y)
                dicc[lista1[indice]].append(y)
    return dicc

DICCIONARIO = read_file('bolsa.csv')

def monthly_average(llave):
    """
    Toma una clave del diccionario y devuelve dos listas: una con las fechas y otra con
    los promedios mensuales
    
    Entrada:
        llave: La clave (accion) del diccionario que quieres promediar
    Salida: 
        una lista de fechas y una lista de promedios.
    """
    fechas = []
    promedios_mes = []
    i = 0 #posicion de las fechas
    mesSeleccionado = DICCIONARIO['Date'][0].split('-')[1] #empiezo en la primera fecha
    fechas.append(DICCIONARIO['Date'][0])
    contadorMeses = 0 #contador aparicion meses
    sumaValoresAccion = 0
    for x in DICCIONARIO['Date']:
        listaFecha = x.split('-')
        if listaFecha[1] != mesSeleccionado:
            promedio = sumaValoresAccion/contadorMeses
            promedios_mes.append(promedio)
            contadorMeses = 0
            sumaValoresAccion = 0
            fechas.append(x)
            mesSeleccionado = listaFecha[1]
        contadorMeses+=1
        sumaValoresAccion+=DICCIONARIO[llave][i]
        i+=1
    promedios_mes.append(promedio)      
    return fechas, promedios_mes

def generadorArchivoCsv(Nombrearchivo='monthly_average_SATL.csv'):
    """
    Toma el nombre de un archivo como entrada y devuelve una tupla de dos listas, la primera es una lista de fechas,
    y el segundo es una lista de que contiene el promedio del valor de la accion por mes
    
    Entrada:
        Nombrearchivo: El nombre del archivo que desea crear
    Salida:
        Un archivo csv
    """
    string = ''
    archivo = open(Nombrearchivo,'w') 
    tuplaSATL = monthly_average('SATL')
    contadorPosiciones = 0
    for fecha in tuplaSATL[0]:
        string += fecha + ',' + str(tuplaSATL[1][contadorPosiciones]) + '\n'
        contadorPosiciones += 1
    archivo.write(string)
    archivo.close() 


    
def max_gain(nombreAccion,dic_datos, fechaVenta): #DONDE DEBERIA USAR DICCIONARIO
    
    
    meses = dic_datos['Date'] #diccionario de fechas
    indice_fecha_venta_original = meses.index(fechaVenta) #me devuelve el indice de la fecha seleccionada (en este caso = 177)
    precios_acciones = dic_datos[nombreAccion] #diccionario precios de la accion elegida
    precio_venta = dic_datos[nombreAccion][indice_fecha_venta_original] #devuelve el precio de venta original
    precio_compra = min(precios_acciones[0:indice_fecha_venta_original]) #a partir de la lista de precios busca el que fue mas barato hasta el momento de venta
    indice_precio_compra = precios_acciones.index(precio_compra) #devuelve el indice del precio donde hubiera sido mejor comprar
    fecha_precio_compra = dic_datos['Date'][indice_precio_compra] #me devuelve la fecha donde hubiera sido mejor comprar
    
    if precio_compra < precio_venta:
        ganancia = (precio_venta-precio_compra)/precio_compra
        return fecha_precio_compra, ganancia
    
    else:
        return print(f'No se ha generado ganancia alguna')
    


 
    
    
    

    

    


     
            
            

        




        
        
    
    
    
    


    
    

    
    
    
                    
                    
                
                
                                
            
            
        


        

        



    
    



""" >>>> ESCRIBAN SU CÓDIGO A PARTIR DE AQUÍ >>>> """



