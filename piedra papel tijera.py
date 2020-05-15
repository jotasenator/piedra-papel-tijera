

import random
import time
import pandas as pd

print('Este es el juego Piedra - Papel - Tijera.')
time.sleep(1)
print('Para elejir Piedra escoja : 1')
time.sleep(1)
print('Para elejir Papel escoja : 2')
time.sleep(1)
print('Para elejir Tijera escoja : 3')
time.sleep(1)
print()
input('...presione enter cuando este listo...')
print()


def Todo():

    contador = 1

    resultadoT = [0, 0, 0]

    while True:

        D = {1: 'Piedra', 2: 'Papel', 3: 'Tijera'}

        try:

            opcion = int(input('Teclee su opción: '))

        except ValueError:

            print()
            print('por favor teclee 1 o 2 o 3...')
            print()
            Todo()

        while opcion != 1 and opcion != 2 and opcion != 3:

            Todo()

        PC_option = random.choice(range(1, 4))

        print()
        print('Ronda {} '.format(contador))

        if PC_option == opcion:

            print()
            time.sleep(1)
            print('Usted ha escogido {}'.format(D[opcion]))
            time.sleep(1)
            print('La PC ha escogido {}'.format(D[PC_option]))
            time.sleep(1)
            print('El resultado es empate...')
            time.sleep(1)
            print('... vamos otra vez...')
            print()
            resultado = [0, 0, 1]

        elif PC_option == 1 and opcion == 2 or PC_option == 2 and opcion == 3 or PC_option == 3 and opcion == 1:

            print()
            time.sleep(1)
            print('Usted ha escogido {}'.format(D[opcion]))
            time.sleep(1)
            print('La PC ha escogido {}'.format(D[PC_option]))
            time.sleep(1)
            print('Ha ganado Usted')
            print()
            resultado = [1, 0, 0]

        elif PC_option == 2 and opcion == 1 or PC_option == 3 and opcion == 2 or PC_option == 1 and opcion == 3:

            print()
            time.sleep(1)
            print('Usted ha escogido {}'.format(D[opcion]))
            time.sleep(1)
            print('La PC ha escogido {}'.format(D[PC_option]))
            time.sleep(1)
            print('Ha ganado la PC')
            print()
            resultado = [0, 1, 0]

        contador += 1

        resultadoT = [sum(x) for x in zip(resultadoT, resultado)]

        resultado_Dic = {'Resultados': resultadoT}

        df = pd.DataFrame(resultado_Dic, index=['Ud', 'PC', 'Empate'])

        if resultadoT[0]-resultadoT[1] == 2:

            print('Felicitaciones, tienes 2 de diferencia')
            print()

        elif resultadoT[0]-resultadoT[1] == 5:

            print('¡Qué bien!, tienes 5 de diferencia')
            time.sleep(1)
            print(' ¿...es dificil verdad?')
            print()

        elif resultadoT[0]-resultadoT[1] == 10:

            print(
                'Debe gustarte mucho este juego...enviame un PrintScreen de esa imagen...')
            time.sleep(1)
            print('jotasenator@gmail.com')
            time.sleep(1)
            print('...lo publicaré en mi facebook junto a la bandera de tu país.')
            print()

        elif resultadoT[0]-resultadoT[1] >= 11:

            print('No puedo creerlo...¡Pics..pics!')
            time.sleep(1)
            print('...hay que retar a los demásssss')
            print()

        print((df).T)
        print()


Todo()
