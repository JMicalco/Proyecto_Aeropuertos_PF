import time #Fecha y Hora

def aeropuertos_pais(pais):   #1
    try:
        archivo=open("airports.dat",'r',encoding="UTF-8")
    except IOError:
        print("Error al abrir el archivo")
    else:
        pais=pais.title()
        print("Aeropuerto\t\t\t\t\tCiudad\t\t\tCodigo")
        for lineas in archivo:
            lista=lineas.split(",")
            if pais in lista[3]:
                #print(lista)   #imprimir aeropuertos de un pais
                print("{0}\t\t\t{1}\t\t{2}" .format(lista[1],lista[2],lista[4]))
        #print("\n",time.strftime("%x %X"))  #Imprimir Fecha y Hora
        archivo.close()

aeropuertos_pais(input("De que pais quieres ver los aeropuertos que hay: "))
