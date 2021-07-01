rom math import floor

numero_prendas = int(input())


def tiempo_preparacion(prendas):
    """Funcion que devuelve el tiempo de preparaacion de las prendas
    el cual es 1 minuto por cada prenda"""
    return prendas


def tiempo_lavado(prendas):
    """Funcion que devuelve el tiempo de lavado de las prendas el cual es el doble del numero de prendas mas 4 minutos"""
    return prendas*2 + 4


def tiempo_secado(tiempo_lavado, tiempo_preparacion):
    """Funcion que devuelve el tiempo de secado de cada tanda y equivale a la quinta parte de la suma del tiempo de laavao y preparacion"""
    return floor((tiempo_lavado+tiempo_preparacion)/5)


def numero_prensistas(tiempo_secado):
    """Funcion que devuelve un string con el numero de prensistas necesarios de acuerdo aal tiiempo de secado de las prendas"""
    if tiempo_secado <= 20:
        return 'uno'
    elif 20 < tiempo_secado <= 30:
        return 'dos'
    elif 30 < tiempo_secado <= 50:
        return 'tres'
    elif tiempo_secado > 50:
        return 'cuatro'


tiempo_preparacion = tiempo_preparacion(numero_prendas)

tiempo_lavado = tiempo_lavado(numero_prendas)

tiempo_secado = tiempo_secado(tiempo_lavado, tiempo_preparacion)

numero_prensistas = numero_prensistas(tiempo_secado)

print('{} {} {}'.format(tiempo_preparacion, tiempo_lavado, tiempo_secado))
print('{}'.format(numero_prensistas))
