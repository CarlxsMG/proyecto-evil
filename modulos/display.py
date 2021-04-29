import os, time
clear = lambda: os.system('cls')
from pynput.keyboard import Listener


def display(texto,opciones):

    def pantalla(texto,opciones):       

        arriba_izq="╔"
        abajo_izq="╚"
        arriba_der="╗"
        abajo_der="╝"
        central_izq="╠"
        central_der="╣"
        central="═"
        vertical="║"
        espacio = " "

        patron_arriba = arriba_izq+(central*198)+arriba_der
        patron_espacio = vertical+(espacio*198)+vertical
        patron_central = central_izq+(central*198)+central_der
        patron_bajo = abajo_izq+(central*198)+abajo_der

        menu = []
        textos = []

        menu.append(patron_arriba)
        for i in range(3):
            menu.append(patron_espacio)
        
        for j in range(int(len(texto)/160)+1):

            if len(texto[j*160:160*(j+1)]) < 160:
                textos.append(espacio+texto[j*160:]+(espacio*(160-len(texto[j*160:])))+espacio)
            else :
                textos.append(espacio+texto[j*160:160*(j+1)]+espacio)
                
        
        for i in textos:
            menu.append(vertical+(espacio*18)+i+(espacio*18)+vertical)
        
        for j in range(3):
            menu.append(patron_espacio)
        
        menu.append(patron_central)


        for j in range(2):
            menu.append(patron_espacio)

        for i in opciones:
            if "-" in i:
                menu.append(vertical+i.center(206, " ")+" "+vertical)

            else:
                menu.append(vertical+i.center(198, " ")+vertical)


        for j in range(2):
            menu.append(patron_espacio)

        menu.append(patron_bajo)
        
        for i in menu:
            print(i)

        if len(menu) < 25:
            print("\n"*(25-len(menu)))


    def check_key(key):
        global opciones_default
        global enterKey
        
        key = str(key).replace("'", "")

        for i in range(len(opciones)):
            if "-" in opciones[i]:
                posicion = i
                break

        if key == "Key.up":
            if posicion > 0:
                opciones[posicion] = (opciones[posicion])[8:-5]
                opciones[posicion-1] = "\x1b[31m - "+opciones_default[posicion-1] + "\x1b[0m "
            else:
                pass
            
                    
        elif key == "Key.down":
            if posicion == len(opciones)-1:
                pass
            else:
                opciones[posicion] = (opciones[posicion])[8:-5]
                opciones[posicion+1] = "\x1b[31m - "+opciones_default[posicion+1] + "\x1b[0m "

        elif key == "Key.enter":
            enterKey = str(posicion)

        else:
            pass

        l.stop()


    global enterKey
    global opciones_default
    enterKey = None

    opciones[0] = "\x1b[31m - "+opciones[0]+"\x1b[0m "

    opciones_default = opciones[:]
    opciones_default[0] = (opciones[0])[8:-5]

    clear()

    print("\n"*30)
    print(("\033[F") * 27)

    pantalla(texto,opciones)

    while True:

        with Listener(on_press=check_key) as l:
            l.join()

        print(("\033[F") * 27)
        pantalla(texto,opciones)

        if enterKey != None:
            break


    return enterKey
    

    




