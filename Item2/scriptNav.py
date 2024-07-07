import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
key = "6d1a6f44-213b-4d21-a528-a6893b21afd4"

def transL8(vehiculo):
    while vehiculo == "":
        vehiculo = input("Ingrese el método de transporte nuevamente: ")
    if vehiculo == "auto" or vehiculo == "car" or vehiculo == "carro" or vehiculo == "automovil" or vehiculo == "automóvil":
        vehicle = "car"
        return vehicle
    elif vehiculo == "bicicleta" or vehiculo == "bike" or vehiculo == "bici" or vehiculo == "bmx" or vehiculo == "cleta":
        vehicle = "bike"
        return vehicle
    elif vehiculo == "pie" or vehiculo == "foot":
        vehicle = "foot"
        return vehicle
    else:
        vehicle = "car"
        print("Método de transporte no reconocido. Se utilizará automóvil.")
        return vehicle


def geocoding(ubicación, key):


    while ubicación == "":
        ubicación = input("Ingresa la ubicación nuevamente: ")
    


    geo_url = "https://graphhopper.com/api/1/geocode?"
    url = geo_url + urllib.parse.urlencode({"q":ubicación, "limit":"1", "key":key})



    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code
    # aquí iba el print con el url y la ubicación? va a aparecer más abajo

    if json_status == 200:
        json_data = requests.get(url).json()
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        nombre = json_data["hits"][0]["name"]
        valor = json_data["hits"][0]["osm_value"]

        if "country" in json_data["hits"][0]:
            país = json_data["hits"][0]["country"]
        else:
            país = ""

        if len(país) !=0:
            nueva_ubi = nombre + ", " + país
        else:
            nueva_ubi = nombre
        
        #print("Información de: " + nueva_ubi + " (Tipo de ubicación: " + valor + ")\n" + url)
    else:
        lat = "null"
        lng = "null"
        nueva_ubi = ubicación
    return json_status,lat,lng,nueva_ubi



while True:
    print("##############################################")
    print("##    Métodos de transporte disponibles     ##")
    print("##            auto, bicicleta, pie          ##")
    print("##############################################")
    

    metTrans = input("Ingrese su método de transporte: ")
    if metTrans == "s":
        break
    vehicle = transL8(metTrans)


    lugar1 = input("Ingrese el lugar de origen: ")
    if lugar1 == "s":
        break
    origen = geocoding(lugar1, key)

    lugar2 = input("Ingrese el lugar de destino: ")
    if lugar2 == "s":
        break
    destino = geocoding(lugar2, key)

    # en el siguiente bloque:
    # coordOrigen: lat y long del origen
    # coordDestino: lat y long del destino
    # paths_url: url para obtener ruta entre origen y destino
    # paths_status: el código de estado que devuelve url_camino
    # paths_data: datos JSON devueltos por el url_camino

    print("================================")
    print("Indicaciones de " + origen[3] + " a " + destino[3] + " en " + metTrans)
    print("================================")
    

    if origen[0] == 200 and destino[0] == 200:
        coordOrigen = "&point="+str(origen[1])+"%2C"+str(origen[2])
        coordDestino = "&point="+str(destino[1])+"%2C"+str(destino[2])
        paths_url = route_url + urllib.parse.urlencode({"key":key, "vehicle":vehicle}) + coordOrigen + coordDestino
        paths_status = requests.get(paths_url).status_code
        paths_data = requests.get(paths_url).json()
        #print("Estado del API de Ruta: " + str(paths_status) + "\nURL del API de Ruta:\n" + paths_url)
    
    if paths_status == 200:
        km = (paths_data["paths"][0]["distance"])/1000          # Conversión de m a km
        mile = float(km)/1.609                                  # Millas
        hora = int(paths_data["paths"][0]["time"]/1000/60/60)
        minuto = int(paths_data["paths"][0]["time"]/1000/60%60)
        segundo = int(paths_data["paths"][0]["time"]/1000%60)
        print("Distancia a recorrer: {0:.2f} km".format(km) + " / {0:.2f} millas".format(mile))

#FALLBACK        print("Distancia a recorrer (métrico): {0:.2f} km".format(km)) 
#FALLBACK        print("Distancia a recorrer (imperial): {0:.2f} millas".format(mile))

        print("Duración del viaje: {0:02d}:{1:02d}:{2:02d}".format(hora, minuto, segundo))


        for each in range(len(paths_data["paths"][0]["instructions"])):
            path = paths_data["paths"][0]["instructions"][each]["text"]
            distance = paths_data["paths"][0]["instructions"][each]["distance"]
            print("================================")
            print("{0} ({1:.2f} km / {2:.2f} millas)".format(path, distance/1000, distance/1000/1.609))
            




#    print(origen)
#    print("--------------------------------")
#    print(destino)
#    print("================================")


