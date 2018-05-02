import time #Fecha y Hora
import math

def distancia_aeropuertos(pais_origen,origen,pais_destino,destino):    #2
    try:
        archivo=open("airports.dat",'r',encoding="UTF-8")
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

pais_origen=input("De que pais sales: ")
origen=input("De que ciudad sales: ")
pais_destino=input("Hacia que pais vas: ")
destino=input("Hacia que ciudad vas: ")
distancia_aeropuertos(pais_origen,origen,pais_destino,destino)
