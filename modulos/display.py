import os, time, sys
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

        patron_arriba = arriba_izq+(central*148)+arriba_der
        patron_espacio = vertical+(espacio*148)+vertical
        patron_central = central_izq+(central*148)+central_der
        patron_bajo = abajo_izq+(central*148)+abajo_der

        menu = []
        textos = []

        menu.append(patron_arriba)
        for i in range(3):
            menu.append(patron_espacio)
        
        for j in range(int(len(texto)/110)+1):

            if len(texto[j*110:110*(j+1)]) < 110:
                textos.append(espacio+texto[j*110:]+(espacio*(110-len(texto[j*110:])))+espacio)
            else :
                textos.append(espacio+texto[j*110:110*(j+1)]+espacio)
                
        
        for i in textos:
            menu.append(vertical+(espacio*18)+i+(espacio*18)+vertical)
        
        for j in range(3):
            menu.append(patron_espacio)
        
        menu.append(patron_central)


        for j in range(2):
            menu.append(patron_espacio)

        for i in opciones:
            if "-" in i:
                menu.append(vertical+i.center(156, " ")+" "+vertical)

            else:
                menu.append(vertical+i.center(148, " ")+vertical)


        for j in range(2):
            menu.append(patron_espacio)

        menu.append(patron_bajo)
        
        for i in menu:
            print(i)

        print(("\033[F") * (len(menu)+1))


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
    clave = None

    opciones[0] = "\x1b[31m - "+opciones[0]+"\x1b[0m "

    opciones_default = opciones[:]
    opciones_default[0] = (opciones[0])[8:-5]

    clear()
    print()

    pantalla(texto,opciones)

    while True:

        with Listener(on_press=check_key) as l:
            l.join()

        if enterKey != None:

            for i in range(len(opciones)):
                if "\x1b[31m" in opciones[i]:
                    clave = i
                    
        if clave != None:
            break

        pantalla(texto,opciones)

    return clave
    
def type_text(texto):
    clear()
    print()

    linea = texto.split(" ")
    new_line = " "
    lineas = []
    point = 0
           
    for j in linea:
        if len(new_line) > 50:
            new_line += j
            lineas.append(new_line)
            new_line = ""
        else:
            new_line += j+" "
    lineas.append(new_line)

    for txt in lineas: 
        for letra in txt:
            # si el carácter es diferente a un punto o existen puntos supensivos, se printean las letras una seguida de otras
            if letra != "." or "..." in txt:
                print(letra, end='') 
                # sys.stdout.flush() Borra el bufer permitiendo no tener que esperar a que se ejecute todo el timpo de espera.
                sys.stdout.flush() 
                time.sleep(0.02) 
            else:
                print(letra)
                time.sleep(0.02)
                point+=1

        if letra != ".":
            print("\n ",end="")
            point+=1
        else:
            print(" ",end="")

    print(("\033[F") * (len(lineas)+point))

def niveles(texto,opciones,diccionario):
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

        patron_arriba = arriba_izq+(central*148)+arriba_der
        patron_espacio = vertical+(espacio*148)+vertical
        patron_central = central_izq+(central*148)+central_der
        patron_bajo = abajo_izq+(central*148)+abajo_der

        menu = []
        textos = []

        menu.append(patron_arriba)
        for i in range(3):
            menu.append(patron_espacio)
        
        for j in range(int(len(texto)/110)+1):

            if len(texto[j*110:110*(j+1)]) < 110:
                textos.append(espacio+texto[j*110:]+(espacio*(110-len(texto[j*110:])))+espacio)
            else :
                textos.append(espacio+texto[j*110:110*(j+1)]+espacio)
                
        
        for i in textos:
            menu.append(vertical+(espacio*18)+i+(espacio*18)+vertical)
        
        for j in range(3):
            menu.append(patron_espacio)
        
        menu.append(patron_central)


        for j in range(2):
            menu.append(patron_espacio)

        for i in opciones:
            if "-" in i:
                menu.append(vertical+i.center(156, " ")+" "+vertical)

            else:
                menu.append(vertical+i.center(148, " ")+vertical)


        for j in range(2):
            menu.append(patron_espacio)

        menu.append(patron_bajo)
        
        for i in menu:
            print(i)

        print(("\033[F") * (len(menu)+1))


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
                if int(opciones[posicion-1]) in diccionario.values():
                    color = "\x1b[32m"
                else:
                    color = "\x1b[31m"
                opciones[posicion-1] = color+" - "+opciones_default[posicion-1] + "\x1b[0m "
            else:
                pass
            
                    
        elif key == "Key.down":
            if posicion == len(opciones)-1:
                pass
            else:
                opciones[posicion] = (opciones[posicion])[8:-5]
                if int(opciones[posicion+1]) in diccionario.values():
                    color = "\x1b[32m"
                else:
                    color = "\x1b[31m"
                opciones[posicion+1] = color+" - "+opciones_default[posicion+1] + "\x1b[0m "

        elif key == "Key.enter":
            enterKey = str(posicion)
            

        else:
            pass
        
        l.stop()

    global enterKey
    global opciones_default
    global color
    color = "\x1b[31m"
    enterKey = None
    clave = None

    opciones[0] = color+" - "+opciones[0]+"\x1b[0m "

    opciones_default = opciones[:]
    opciones_default[0] = (opciones[0])[8:-5]

    clear()
    print()

    pantalla(texto,opciones)

    while True:

        with Listener(on_press=check_key) as l:
            l.join()

        if enterKey != None:

            for i in range(len(opciones)):
                if color in opciones[i]:
                    clave = i
                    
        if clave != None:
            break

        pantalla(texto,opciones)

    return clave


