from playsound import playsound
import time
from pathlib import Path
import sys

url = (str(Path(__file__).parent.absolute())).split("\\")
url.pop(-1)
url = "\\".join(url)

sys.path.append(url)

from modulos.display import *
from modulos.inventario import Inventario


###################| ZONA DE PRUEBAS |#####################
inventario = Inventario(4)
inventario.añadirObjeto("Flauta")
inventario.añadirObjeto("Orbe")
###########################################################



def Sala3(inventario):

    game = True

    type_text("Te adentras por un camino un tanto angosto de paredes escarpadas, entre ellas va resonando una melodia a lo lejos que incrementa su volumen a medida que te acercas. El pasillo va ganando anchura y tamaño hasta que llegas a una gran sala con forma de cupula, en el centro de ella puedes ver un lago el cual piensas que debe emanar sus aguas desde las entrañas de la montaña. Es ahora cuando ves en la orilla una sirena que interpreta la melodía que escuchabas durante todo el camino.")

    while game:

        opciones = ["Salir","Inspeccionar","Acercarse a ..."]
        texto="Al llegar a la sala... "
        
        if display(texto,opciones) == 0:          
        # OPCION SALIR
            break

        elif display(texto,opciones) == 1:
        # OPCION "INSPECCIONAR"
            os.system("cls")
            texto="Observas en el centro del lago un altar con un orbe, están totalmente congelados son un bloque de hielo. A tu derecha apoyado sobre la pared ves una pequeña y vieja barca para una persona."
            opciones = ["Inspeccionar la barca"]
            
            if display(texto,opciones) == 0:
            # OPCION "INSPECCIONAR LA BARCA"
                texto="La barca es muy antigua pero no parece estar rota puede servir para llegar hasta el altar."
                opciones = ["Llevar la barca al agua"]
                
                if display(texto,opciones) == 0:
                # OPCION "LLEVAR LA BARCA AL AGUA"
                    texto="Agarras la barca la vuelcas hacia el suelo y la arrastras hasta el agua, una vez allí te fijas que en el interior de la barca hay lo que parece un pequeño saco de monedas. Al comprobar su contenido encuentras 9 monedas de oro."
                    inventario.añadirObjeto(["Saco de monedas"])     # Añadimos el dinero recogido al inventario //////// A LA ESPERA DE MODIFICAR ////////
      
        elif display(texto,opciones) == 2:         
        # OPCION ACERCARSE A...
            opciones = ["Salir","Sirena","Orbe"]        # Se enumera para elegir por le usuario como 0.. 1... 2...
            texto = "  "
            if display(texto,opciones) == 0:
            # OPCION SALIR
                return
            
            elif display(texto,opciones) == 1:
            # OPCION ACERCARSE A LA SIRENA
            
                if inventario.buscarObjeto(["Flauta"]) == True:
                # SI TENEMOS LA FLAUTA EN EL INVENTARIO RECOGIDA EN LA SALA2
                    texto="Te acercas lentamente a la sirena la cual canta con más intensidad.. tal vez podrías..."
                    opciones = ["Salir", "Acompañar la melodía"]
                    
                    if display(texto,opciones) == 0:
                    # OPCION SALIR
                        return

                    elif display(texto,opciones) == 1:
                    # OPCION ACOMPAÑAR LA MELODIA
                        type_text("Una voz y una melodía te invaden y acompañas sin ninguna dote musical a la sirena.")
                        playsound("../musica/sonido_flauta.mp3")
                        time.sleep(10)
                        type_text("La sirena se horroriza con la musica..")
                        time.sleep(10)
                        type_text("La sirena no puede soportarlo está aturdida")
                        time.sleep(10)
                        type_text("Empieza a llorar sus lagrimas son diferentes brillan como si fuesen mágicas, tal vez tengan algun poder curativo..")
                        opciones = ["Salir","Recoger en un frasco"]
                        
                        if display(texto,opciones) == 0:
                        # OPCION SALIR
                            return

                        elif display(texto,opciones) == 1:
                        # OPCION RECOGER EN UN FRASCO
                            type_text("Sacas el frasco de tu bolsa y recoges unas pocas lágrimas de la sirena ella todavia aturdida se da la vuelta y se zambulle en el agua, no creo que vuelvas a verla... Las lágrimas de sirena tienen poderes curativos muy potentes son altamente efectivas contra venenos potentes y son muy dificiles de encontrar seguro que pagarian un buen precio por ellas.")
                            inventario.añadirObjeto(["Frasco con lagrimas"])
                            #inventario.remove(["Frasco vacío"])

                else:
                # SI NO TENEMOS LA FLAUTA NECESARIA PARA COMPLETAR EL NIVEL.
                    type_text("Te acercas lentamente a la sirena, ella deja de cantar y en su lugar chilla fuerte y agudo tan fuerte que incluso llega a aturdirte. Las sirenas solo entienden el lenguaje de la música.")
                    opciones = ["Salir","Acercarse a ..."]

            elif display(texto,opciones) == 2:
            # OPCION ACERCARSE AL ORBE
                
                if inventario.buscarObjeto(["Flauta"]) == True and inventario.buscarObjeto(["Cubo salitre"]):
                # SI DISPONEMOS DE LA FLAUTA Y ADEMAS DEL CUBO DE SALITRE RECOGIDO EN LA SALA4
                    type_text("Montas en la barca y remas lentamente hasta llegar al altar.")
                    opciones = ["Volver a la orilla", "Usar cubo de salitre"]

                    if display(texto,opciones) == 0:
                    # OPCIÓN "VOLVER A LA ORILLA"
                        return

                    if display(texto,opciones) == 1:
                    # OPCION "USAR CUBO DE SALITRE"
                        type_text("Viertes el salitre sobre el hielo del altar y rapidamente ¡empieza a descongelarse!, recoges el orbe del agua.")
                        inventario.añadirObjeto(["Orbe del Agua"])

                elif inventario.buscarObjeto(["Flauta"]) == True:
                # SI SOLO DISPONEMOS DE LA FLAUTA PERO NO DEL CUBO DE SALITRE
                    type_text("Compruebas que el orbe está congelado con todo el altar, es una capa gruesa de hielo deberás encontrar la forma de eliminarlo para hacerte con el orbe.")
                else:
                # SI NO DISPONEMOS DE NINGUN OBJETO NECESARIO.
                    type_text("Te acercas lentamente a la sirena, ella deja de cantar y en su lugar chilla fuerte y agudo tan fuerte que incluso llega a aturdirte. Las sirenas solo entienden el lenguaje de la música.")

             
    return "EXIT_LEVEL"

Sala3(inventario)