
VLAN = int(input("Ingrese el número de la VLAN: "))

if VLAN >= 0 and VLAN <= 1005:
    print("La VLAN ingresada se encuentra en el rango ESTÁNDAR")
elif VLAN >= 1006 and VLAN <= 4094:
    print("La VLAN ingresada se encuentra en el rango EXTENDIDO")
else:
    print("La VLAN ingresada no es válida.")