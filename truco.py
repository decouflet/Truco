import random

valores = {(4, "copa"): 10, (4, "espada"): 10, (4, "basto"): 10, (4, "oro"): 10, (5, "copa"): 20, (5, "espada"): 20,
            (5, "basto"): 20, (5, "oro"): 20, (6, "copa"): 30, (6, "espada"): 30, (6, "basto"): 30, (6, "oro"): 30,
            (7, "copa"): 40, (7, "basto"): 40, (10, "copa"): 50, (10, "espada"): 50, (10, "basto"): 50, (10, "oro"): 50,
            (11, "copa"): 60, (11, "espada"): 60, (11, "basto"): 60, (11, "oro"): 60, (12, "copa"): 70, (12, "espada"): 70,
            (12, "basto"): 70, (12, "oro"): 70, (1, "copa"): 80, (1, "oro"): 80, (2, "copa"): 90, (2, "espada"): 90,
            (2, "basto"): 90, (2, "oro"): 90, (3, "copa"): 100, (3, "espada"): 100, (3, "basto"): 100, (3, "oro"): 100,
            (7, "oro"): 110, (7, "espada"): 110, (1, "basto"): 120, (1, "espada"): 130}


opciones = ["tirar carta", "truco", "envido", "irme al maso"]


def repartir_usario_1(numeros, palos):
    mano = []
    for carta in range(3):
        carta_numero = random.choice(numeros)
        carta_palo = random.choice(palos)
        for cart in mano:
            while cart[0] == carta_numero and cart[1] == carta_palo:
                carta_numero = random.choice(numeros)
                carta_palo = random.choice(palos)
        mano.append((carta_numero, carta_palo))
    return mano


def repartir_usuario_2(numeros, palos, mano_compu):
    mano = []
    for carta in range(3):
        carta_numero = random.choice(numeros)
        carta_palo = random.choice(palos)
        for cart in mano:
            while cart[0] == carta_numero and cart[1] == carta_palo:
                carta_numero = random.choice(numeros)
                carta_palo = random.choice(palos)
        for car in mano_compu:
            while car[0] == carta_numero and car[1] == carta_palo:
                carta_numero = random.choice(numeros)
                carta_palo = random.choice(palos)
        mano.append((carta_numero, carta_palo))
    return mano


def calculador_de_puntos(mano):
    combinaciones = [[0, 0], [0, 1], [1, 1]]
    puntos = []
    numeros = []
    palos = []
    for carta in mano:
        palos.append(carta[1])
        numeros.append(carta[0])
    for par in combinaciones:
        if palos[0 + par[0]] == palos[1 + par[1]]:
            if numeros[0 + par[0]] > 7 and numeros[1 + par[1]] > 7:
                punto = 20
                puntos.append(punto)
            elif numeros[0 + par[0]] > 7 and numeros[1 + par[1]] < 7:
                punto = 20 + numeros[1 + par[1]]
                puntos.append(punto)
            elif numeros[0 + par[0]] < 7 and numeros[1 + par[1]] < 7:
                punto = 20 + numeros[0 + par[0]] + numeros[1 + par[1]]
                puntos.append(punto)
    return max(puntos)


def empezar_partida(mano_usuario):
    print(f"Esta es su mano: {mano_usuario}")
    print(opciones)
    opcion = input("Cual es su jugada?")
    while opcion not in opciones:
        opcion = input("La opcion que elijio no es valida, por favor elija otra: ")
    if opcion == "tirar carta":
        carta = int(input("Aprete 1, 2 o 3 dependiendo la carta que desee tirar: "))
        return [opcion, mano_usuario[carta-1], carta]
    else:
        return [opcion]


def segunda_jugada(jugada_usuario_1, mano_usuario_2, mano_usuario_1):
    if jugada_usuario_1[0] == "tirar carta":
        print(f"Te tiraron un {jugada_usuario_1[1]}")
        mano_usuario_1.pop([jugada_usuario_1[2] - 1])
        decision = empezar_partida(mano_usuario_2)
        decision.insert(0, "tirar carta")
        return decision
    elif jugada_usuario_1[0] == "truco":
        print(f"Esta es tu mano: {mano_usuario_2}")
        decision = input("Te cantaron truco amigo, vas a querer? si/no : ")
        if decision == "si":
            re_truco = input("Le queres cantar she truco? si/no: ")
            if re_truco == "si":
                return ["truco", decision, re_truco]
            elif re_truco == "no":
                return ["truco", decision, re_truco]
        else:
            return ["truco", decision]
    elif jugada_usuario_1[0] == "envido":
        print(f"Esta es tu mano: {mano_usuario_2}")
        decision = input("Te cantaron envido amigo, vas a querer? si/no : ")
        if decision == "si":
            puntos = calculador_de_puntos(mano_usuario_2)
            return ["envido", decision, puntos]
        else:
            return ["envido", decision]


def tercer_jugada(jugada_usuario_2, mano_usuario_1, mano_usuario_2):
    if jugada_usuario_2[0] == "tirar carta":
        if jugada_usuario_2[1] == "tirar carta":
            print(f"Te tiraron un: {jugada_usuario_2[2]}")
            print(opciones[:2])
            decision = input("Que vas a hacer?")
            while decision not in opciones[:2]:
                decision = input("La decision que ingresó no es valida, por favor intente otra vez: ")
            if decision == "tirar carta":
                print(f"Esta es tu mano: {mano_usuario_1}")
                carta = int(input("Ingrese el numero de la carta que desea 1, 2"))
                return ["tirar carta", "tirar carta", decision, mano_usuario_1[carta - 1]]
            elif decision == "truco":
                return ["tirar carta", "tirar carta", decision]
        elif jugada_usuario_2[1] == "truco":
            decision = input("Te cantaron truco, vas a querer? si/no: ")
            return ["tirar carta", "truco", decision]
        elif jugada_usuario_2[1] == "envido":
            decision = input("Te cantaron truco, vas a querer? si/no: ")
            return ["tirar carta", "envido", decision]
    elif jugada_usuario_2[0] == "truco":
        if jugada_usuario_2[1] == "si":
            if jugada_usuario_2[2] == "no":
                print("Te quisieron el truco")
                print(mano_usuario_1)
                carta_usuario_1 = int(input("Aprete 1, 2 o 3 dependiendo que carta desea tirar: "))
                print(mano_usuario_1[carta_usuario_1 - 1])
                print("Que le vas a tirar?")
                print(mano_usuario_2)
                carta_usuario_2 = int(input("Aprete 1, 2 o 3 dependiendo que carta desea tirar: "))
                print(mano_usuario_2[carta_usuario_2 - 1])
                if valores[mano_usuario_1[carta_usuario_1 - 1]] > valores[mano_usuario_2[carta_usuario_2 - 1]]:
                    print("Gana la primer ronda el usuario_1")
                    return ["truco", "si", "no", "usuario_1"]
                elif valores[mano_usuario_1[carta_usuario_1 - 1]] < valores[mano_usuario_2[carta_usuario_2 - 1]]:
                    print("Gana la primer ronda el usuario_2")
                    return ["truco", "si", "no", "usuario_2"]
                else:
                    return ["truco", "si", "no", "parda"]
            elif jugada_usuario_2 == "si":
                print("Te quisieron el truco y encima te cantaron re truco")
                decision_2 = input("Queres el she truco?")
                if decision_2 == "si":
                    return ["truco", "si", "si", decision_2]
                elif decision_2 == "no":
                    return ["truco", "si", "si", decision_2]
        elif jugada_usuario_2[1] == "no":
            return ["truco", "no"]
    elif jugada_usuario_2[0] == "envido":
        if jugada_usuario_2[1] == "si":
            puntos_usuario_1 = calculador_de_puntos(mano_usuario_1)
            print("Te quisieron el envido, cuantos puntos tenes? ")
            print(f"Puntos del usuario_1: {puntos_usuario_1}")
            print(f"Puntos del usuario_2: {jugada_usuario_2[2]}")
            if puntos_usuario_1 > jugada_usuario_2[2]:
                return "Gana el envido el usuario_1"
            elif puntos_usuario_1 < jugada_usuario_2[2]:
                return "Gana el envido el usuario_2"



def main():
    numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ["basto", "oro", "espada", "copa"]
    mano_usuario_1 = repartir_usario_1(numeros, palos)
    mano_usuario_2 = repartir_usuario_2(numeros, palos, mano_usuario_1)
    jugada_usuario_1 = empezar_partida(mano_usuario_1)
    if jugada_usuario_1[0] != "irme al maso":
        jugada_usuario_2 = segunda_jugada(jugada_usuario_1, mano_usuario_2, mano_usuario_1)
    jugada_usuario_1_1 = tercer_jugada(jugada_usuario_2, mano_usuario_1, mano_usuario_2)


main()