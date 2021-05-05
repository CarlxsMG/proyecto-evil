from pathlib import Path
import sys
import os
from playsound import playsound

clear= lambda:os.system("cls")

url = (str(Path(__file__).parent.absolute())).split("\\")
url.pop(-1)
url = "\\".join(url)

sys.path.append(url)

from modulos.display import display
from modulos.inventario import Inventario


while True:
    playsound("../musica/biblioteca.mp3",False)
    """*********************** SE DUPLICA,TRIPLICA ETC... EL SONIDO CADA VEZ QUE SE SELECCIONA "Salir" ***********************"""
    while True:
        texto="Estas en una sala amplia, en la que destaca una estatua central, estanterias con libros antiguos y polvorientos a un lado, y al otro, una larga mesa con papeles."
        opciones=["Acercarse a..","Examinar..","Salir.."]
        if display(texto,opciones)==0:
            clear()
            texto="¿Donde te gustaria acercarte?"
            opciones=["Estanterias..","Estatua..","Escritorio..","Salir.."]
            if display(texto,opciones)==0:
                clear()
                texto="Tienes delante una gran cantidad de libros viejos, algunos de ellos ilegibles por la degradación de la humedad y del tiempo."
                opciones=["Examinar..","Salir.."]
                if display(texto,opciones)==0:
                    clear()
                    texto="Una nota sobresale de entre los libros, parece haber sido usada recientemente."
                    opciones=["Leer nota..","Salir.."]
                    if display(texto,opciones)==0:
                        texto="::NOTA:: 'Cuando cumplí los cincuenta nació mi primer nieto.-Ahora que voy camino de cumplir los setenta tengo muchos más.' “Cada uno de mis hijos tiene tantos hijos como hermanos y el número combinado de mis hijos y mis nietos es exactamente mi edad”."
                        opciones=["Salir.."]
                        if display(texto,opciones)==0:
                            break
                    else:
                        break
                else:
                    break
            elif display(texto,opciones)==1:
                """*********************** PREGUNTA DOS VECES "¿Donde te gustaria acercarte? ***********************"""
                clear()
                texto="Una estatua de un hombre que porta dos objetos,uno en cada mano.En la mano derecha una llave bastante desgastada y en la izquierda una extraña caja metálica."
                opciones=["Examinar..","Salir.."]
                if display(texto,opciones)==0:
                    texto="En la base de la estatua puede leerse 'En memoria de Wohn Jick' (...). Justo debajo de la leyenda,se puede ver un mecanismo numérico de dos dígitos"
                    opciones=["Colocar números..","Salir.."]