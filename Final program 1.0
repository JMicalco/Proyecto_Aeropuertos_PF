#Programa de aeropuertos
import time #Fecha y Hora
import math
#Funcion para opcion 1
def aeropuertos_pais(pais):   #1
    try:
        archivo=open("airports.dat.txt",'r',encoding="UTF-8")
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
def distancia_aeropuertos(pais_origen,origen,pais_destino,destino):    #2
    try:
        archivo=open("airports.dat.txt",'r',encoding="UTF-8")
    except IOError:
        print("Error al abrir el archivo")
    else:
        pais_origen=pais_origen.title()
        origen=origen.title()
        pais_destino=pais_destino.title()
        destino=destino.title()
        for lineas in archivo:
            lista=lineas.split(",")
            if pais_origen in lista[3]:
                if origen in lista[2]:
                    #print(lista)
                    aero_origen=lista[1]
                    origen_lat=float(lista[6])
                    origen_lon=float(lista[7])
            if pais_destino in lista[3]:
                if destino in lista[2]:
                    #print(lista)
                    aero_destino=lista[1]
                    destino_lat=float(lista[6])
                    destino_lon=float(lista[7])
                    distancia=formula_haversine(origen_lat,origen_lon,destino_lat,destino_lon)
                    print("La distancia entre el aeropuerto de {0}: {1} en {2} y el aeropuerto de {3}: {4} en {5} es de {6:.3f} km" .format(origen,aero_origen,pais_origen,destino,aero_destino,pais_destino,distancia))
        #print("\n",time.strftime("%x %X"))  #Imprimir Fecha y Hora
        archivo.close()
def formula_haversine(origen_latitud,origen_longitud,destino_latitud,destino_longitud):
    #Convertir grados a radianes
    lat1=math.radians(origen_latitud)
    lon1=math.radians(origen_longitud)
    lat2=math.radians(destino_latitud)
    lon2=math.radians(destino_longitud)
    #Formula de Haversine
    dlon=lon2-lon1
    dlat=lat2-lat1
    a=math.sin(dlat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    c=2*math.asin(math.sqrt(a))
    r=6371 #Radio de la Tierra en km
    distancia=c*r
    return distancia
def opcion_3(pais1):
    n=0
    pais=pais1.capitalize()
    cont=0
    try:
        airlines=open("airports.dat.txt", "r", encoding="UTF-8")
    except IOError:
        print("El fichero no existe")
    else:
        for linea in airlines:
            #lista por cada linea del archivo
            listaA=airlines.readline().split(",")
            for elemento in range(len(listaA)):
                #Eliminando las doble commillas por cada elemento de la Lista
                pais2=listaA[elemento].strip('"')
                #Condicionando para verificar si el pais que ingreso el ususario es igual al elemento seleccionado de la lista
                if pais2==pais or pais2==pais1:
                    #Valores de latitud y longitud
                    lat2=float(listaA[6])
                    lon2=float(listaA[7])
                    nombre=listaA[1]
                    cont+=1
                    #Condicional para guardar los valores de latitud y longitud del primer aeropuerto
                    if cont==1:
                        lat1=lat2
                        lon1=lon2
                        nombre_n=nombre
                    elif cont>=2:
                        try:
                            archivo=open("Reporte_opcion_3.txt", "w+", encoding="UTF-8")
                        except IOError:
                            print("El fichero no existe")
                        else:
                            #Funcion para calcular la distancia entre el primer aeropuerto y los demas
                            def distancia(lat1, lon1, lat2, lon2):
                                rad=math.pi/180
                                del_lat=lat2-lat1
                                del_lon=lon2-lon1
                                R=6372.795477598
                                a=(math.sin(rad*del_lat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*del_lon/2))**2
                                distancia=2*R*math.asin(math.sqrt(a))
                                return distancia
                            mensaje="La distancia entre " +str(nombre_n) + " y " + str(nombre) + "es de " + str(distancia(lat1, lon1, lat2, lon2))+ " km"
                            print(mensaje)
                            archivo.write(mensaje)
                            archivo.close()
        print("Reporte generado")
        airlines.close()
def opcion_4(code_air, destino):
    try:
        rutas_air=open("routes.dat.txt", "r", encoding="UTF-8")
        airlines=open("airlines.dat.txt", "r", encoding="UTF-8")
        airports=open("airports.dat.txt", "r", encoding="UTF-8")
        archivo=open("archivo_reporte_4.txt", "w+", encoding="UTF-8")
    except IOError:
        print("El fichero no existe")
    else:
        lista_code_airline=[]
        lista_vuelos_di=[]
        lista_total=[]
        lista_final=[]
        lista_final1_1=[]
        for linea in rutas_air:
            #Lista por cada linea del archivo de rutas
            lista=linea.split(",")
            #Condicional para verifical que el codigo se encuentre en la linea y que sea de partida
            if code_air==lista[2] and destino==lista[4]:
                #El id de la Aerolinea
                airline_id=lista[1]
                airline_id
                lista_code_airline.append(airline_id)
                if lista[7]=="0":
                    vuelos_di="Sin escalas"
                    lista_vuelos_di.append(vuelos_di)
                else:
                    vuelos_di="Con escalas"
                    lista_vuelos_di.append(vuelos_di)
        for linea in airlines:
            #Lista por cada linea del archivo de Aerolineas
            listaA=linea.split(",")
            for pos in range(len(lista_code_airline)):
                #Condicional para verificar si coinciden los id de las aerolineas
                    if lista_code_airline[pos]==listaA[0]:
                        nombre_air=listaA[1]
                        alias_air=listaA[2]
                        lista_total.append(nombre_air + "- " + alias_air)
                        lista_final1_1.append(nombre_air)
                        lista_final1_1.append(alias_air)
        for n in range(len(lista_total)):
            lista_final.append(lista_total[n])
            lista_final.append(lista_vuelos_di[n])
        #print(lista_final)
        for pos in range(len(lista_final)):
            if pos%2==0:
                archivo.write(lista_final[pos]+"\n")
        rutas_air.close()
        airports.close()
        airlines.close()
        print(lista_final)
    return lista_final
def aerolineas_aeropuerto(nombre):  #5
    try:
        aeropuerto=open("airports.dat.txt",'r',encoding="UTF-8")
    except IOError:
        print("Error al abrir el archivo")
    else:
        try:
            routas=open("routes.dat.txt",'r',encoding="UTF-8")
        except IOError:
            print("Error al abrir el archivo")
        else:
            try:
                aerolineas=open("airlines.dat.txt",'r',encoding="UTF-8")
            except IOError:
                print("Error al abrir el archivo")
            else:
                aerolineas_codigos=[]
                nombre=nombre.title()
                for lineas_a in aeropuerto:
                    lista_a=lineas_a.split(",")
                    if nombre in lista_a[1]:
                        codigo=lista_a[4]
                codigo=codigo.strip('"')    #Quitar comillas a un string
                for lineas_r in routas:
                    lista_r=lineas_r.split(",")
                    if codigo in lista_r[2]:
                        codigo_v=lista_r[1]
                        if codigo_v not in aerolineas_codigos:
                            aerolineas_codigos.append(codigo_v)
                for lineas_v in aerolineas:
                    lista_v=lineas_v.split(",")
                    if lista_v[0] in aerolineas_codigos:
                        if "Y" in lista_v[7]:
                            #print(lista_v)     #Ver aerolineas
                            print(lista_v[1])
        #print("\n",time.strftime("%x %X"))  #Imprimir Fecha y Hora
        aeropuerto.close()
        routas.close()
        aerolineas.close()
def opcion_6(nombre_aerolinea, nombre_aeropuerto):
    try:
        airlines=open("airlines.dat.txt", "r", encoding="UTF-8")
        airports=open("airports.dat.txt", "r", encoding="UTF-8")
        rutas_air=open("routes.dat.txt", "r", encoding="UTF-8")
        archivo=open("Reporte_opcion_6.txt", "w+", encoding="UTF-8")
    except IOError:
        print("El fichero no existe")
    else:
        lista_airline_id=[]
        lista_airport_id=[]
        lista_destination_airport_id=[]
        for lineas in airlines:
            lista_linea=lineas.split(",")
            nombre_aerolinea_sinc=lista_linea[1].strip('"')
            if nombre_aerolinea_sinc==nombre_aerolinea:
                airline_id=lista_linea[0]
                #nombre_aerolinea_final=nombre_aerolinea_sinc
                #lista_airline_id.append(airline_id)
                #print(airline_id)
        for linea in airports:
            lista_linea_2=linea.split(",")
            nombre_aeropuerto_sinc=lista_linea_2[1].strip('"')
            if nombre_aeropuerto_sinc==nombre_aeropuerto:
                airport_id=lista_linea_2[0]
                lat1=float(lista_linea_2[6])
                lon1=float(lista_linea_2[7])
                nombre_aeropuerto_final=nombre_aerolinea_sinc
                #lista_airport_id.append(airport_id)
                #print(airport_id)
        airports.close()
        for linea in rutas_air:
            lista_linea_3=linea.split(",")
            if airline_id==str(lista_linea_3[1]) and airport_id==str(lista_linea_3[3]) and lista_linea_3[7]==str(0):
                destination_airport_id=lista_linea_3[5]
                lista_destination_airport_id.append(destination_airport_id)
                #print(lista_destination_airport_id)
        airports=open("airports.dat.txt", "r", encoding="UTF-8")
        for linea in airports:
            lista_linea_4=linea.split(",")
            for n in range(len(lista_destination_airport_id)):
                #destination_airport_id_id=destination_airport_id.strip('"')
                if lista_destination_airport_id[n]==(lista_linea_4[0]):
                    #print(lista_linea_4[1])
                    lat2=float(lista_linea_4[6])
                    lon2=float(lista_linea_4[7])
                    def distancia(lat1, lon1, lat2, lon2):
                        rad=math.pi/180
                        del_lat=lat2-lat1
                        del_lon=lon2-lon1
                        R=6372.795477598
                        a=(math.sin(rad*del_lat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*del_lon/2))**2
                        distancia=2*R*math.asin(math.sqrt(a))
                        return distancia
                        #mensaje=str(nombre_aeropuerto_final)+ ", "  + str(distancia(lat1, lon1, lat2, lon2))+ " km"
                        print(mensaje)
                    mensaje=str(nombre_aeropuerto_final)+ ", "  + str(distancia(lat1, lon1, lat2, lon2))+ " km"
                    archivo.write(mensaje+"\n")
        #archivo.write(mensaje+"\n")
        archivo.close()
        airlines.close()
        rutas_air.close()
        return mensaje
opcion=1
while opcion !=7:
    print("Programa elaborado por Luis Alberto y José Adolfo")
    print("Menu:")
    print("1. Aeropuertos de un pais")
    print("2. Distancia entre aeropuertos")
    print("3. Distancia entre aeropuertos de un pais")
    print("4. Aerolineas que van a un destino desde un determinado aeropuerto")
    print("5. Aerolíneas que operan en un determinado aeropuerto")
    print("6. Destinos de una aerolínea desde un determinado aeropuerto")
    print("7. Salir")
    opcion=int(input("Ingresa el numero de la opcion "))
    if opcion==1:
        print(aeropuertos_pais(input("De que pais quieres ver los aeropuertos que hay: ")))
    elif opcion==2:
        pais_origen=input("De que pais sales: ")
        origen=input("De que ciudad sales: ")
        pais_destino=input("Hacia que pais vas: ")
        destino=input("Hacia que ciudad vas: ")
        distancia_aeropuertos(pais_origen,origen,pais_destino,destino)
    elif opcion==3:
            pais1=input("Ingresa el nombre del pais (En ingles) ")
            opcion_3(pais1)
    elif opcion==4:
        code_air=input("Ingresa el codigo del aeropuerto de partida ")
        destino=input("Ingresa el codigo del aeropuerto de destino ")
        opcion_4(code_air, destino)
    elif opcion==5:
        nombre=input("De que aeropuerto quieres saber las aerolineas que operan: ")
        aerolineas_aeropuerto(nombre)
    elif opcion==6:
        nombre_aerolinea=input("Ingresa el nombre de la aerolinea ")
        nombre_aeropuerto=input("Ingresa el nombre del aeropuerto ")
        print(opcion_6(nombre_aerolinea, nombre_aeropuerto))
    elif opcion==7:
        print("Saliendo")
    else:
        print("Opcion invalida")
