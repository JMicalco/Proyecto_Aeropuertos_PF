import time #Fecha y Hora

def aerolineas_aeropuerto(nombre):  #5
    try:
        aeropuerto=open("airports.dat",'r',encoding="UTF-8")
    except IOError:
        print("Error al abrir el archivo")
    else:
        try:
            routas=open("routes.dat",'r',encoding="UTF-8")
        except IOError:
            print("Error al abrir el archivo")
        else:
            try:
                aerolineas=open("airlines.dat",'r',encoding="UTF-8")
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

nombre=input("De que aeropuerto quieres saber las aerolineas que operan: ")
aerolineas_aeropuerto(nombre)
