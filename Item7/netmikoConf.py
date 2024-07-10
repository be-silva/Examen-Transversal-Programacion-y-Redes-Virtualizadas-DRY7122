# Prayge

from netmiko import ConnectHandler

# Conexión a Router SalvoSilva
Router = ConnectHandler(
    host = '192.168.56.115',
    username = 'cisco',
    password = 'cisco123!',
    device_type = 'cisco_xe'
)


# 1- Lista de comandos EIGRP Named
comandos_config = [
    # ipv6 unicast
    'ipv6 unicast-routing',

    # Interfaz GigabitEthernet1
    'interface GigabitEthernet1',
    'ipv6 address 3001:AAAA:AAAA:1::1/128',


    # EIGRP IPV4
    'router eigrp AS_SalSil',
    'address-family ipv4 unicast autonomous-system 100',
    'network 192.168.56.115 0.0.0.0',
    'exit-address-family',
    

    # IPV6
    'address-family ipv6 unicast autonomous-system 100',
    'af-interface lo33',
    'passive-interface',
    'exit-af-interface',
    'exit-address-family',



]

print("")
input("1. Se configura EIGRP Nombrado: ") # Prompt para dividir cada segmento de forma más ordenada

primerOut = Router.send_config_set(comandos_config)
print(primerOut)


# 2- Info IPs e Interfaces (show ip int br)
infoIpInt = [
    'exit',
    'show ip int br',
    'show ipv6 int br'
]

print("")
input("2. Se muestra info. sobre direccionamiento en interfaces: ") # Prompt para dividir cada segmento de forma más ordenada

segundoOut = Router.send_config_set(infoIpInt)
print(segundoOut)


# 3- Running-config (show run)

print("")
input("3. Se muestra el running-config: ") # Prompt para dividir cada segmento de forma más ordenada

tercerOut = Router.send_command('show running-config')
print(tercerOut)


# 4- Show version

print("")
input("4. Se muestra el comando \"show version\": ") # Prompt para dividir cada segmento de forma más ordenada

cuartoOut = Router.send_command('show version')
print(cuartoOut)


###heartbeat = Router.is_alive()
###print(heartbeat)