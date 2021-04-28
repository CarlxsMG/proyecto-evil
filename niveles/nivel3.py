def display_acercarse_a():
    opciones = ["Salir","Sirena","Orbe"]

    # display(texto, opciones) returna la opcion elegida "0, 1 o 2"
    if display == "0":      # SALIR
        continue
    
    elif display == "1":    # Acercarse a la SIRENA
    
        if inventario.search(["Flauta"]) == True:
            texto = "Te acercas lentamente a la sirena la cual canta con más intensidad.. tal vez podrías..."
            opciones = ["Salir", "Acompañar la melodía"]
        else:
            texto = "Te acercas lentamente a la sirena, ella deja de cantar y en su lugar chilla fuerte y agudo tan fuerte que incluso llega a aturdirte. Las sirenas solo entienden el lenguaje de la música."
            opciones = ["Salir","Acercarse a ..."]

    elif display == "2":    # Acercarse al ORBE
        
        if inventario.search(["Flauta"]) == True and inventario.search(["Cubo salitre"]):
            texto = 
        elif inventario.search(["Flauta"]) == True:
            texto = "Compruebas que el orbe está congelado con todo el altar es una capa gruesa de hielo deberás encontrar la forma de eliminarlo para hacerte con el orbe."
        else:
            texto = "Te acercas lentamente a la sirena, ella deja de cantar y en su lugar chilla fuerte y agudo tan fuerte que incluso llega a aturdirte. Las sirenas solo entienden el lenguaje de la música."


def Sala3(inventario):

    game = True

    texto = "Te adentras por un camino un tanto angosto de paredes escarpadas, entre ellas va resonando una melodia a lo lejos que incrementa su volumen a medida que te acercas. El pasillo va ganando anchura y tamaño hasta que llegas a una gran sala con forma de cupula, en el centro de ella puedes ver un lago el cual piensas que debe emanar sus aguas desde las entrañas de la montaña. Es ahora cuando ves en la orilla una sirena que interpreta la melodía que escuchabas durante todo el camino."

    while game == True:
        texto = "Al llegar a la sala... "

        opciones = ["Salir","Inspeccionar","Acercarse a ..."]

        if display == "0":
            game = False
            continue

        elif display == "1":
            txt_inspeccionar = "Observas en el centro del lago un altar con un orbe, están totalmente congelados son un bloque de hielo. A tu derecha apoyado sobre la pared ves una pequeña y vieja barca para una persona."
            opciones = ["Salir", "Inspeccionar la barca"]
            
            if display == "0":
                opciones = ["Salir","Acercarse a ..."]

                if display == "0":
                    game = False
                    continue

                elif display == "1":
                    display_acercarse_a()       # Con esta función desplegamos las opciones de acercarse a la sirena y al orbe.
            
            elif display == "1":
                texto = "La barca es muy antigua pero no parece estar rota puede servir para llegar hasta el altar."
                opciones ["Salir","Llevar la barca al agua"]
                
                if display == "0":
                    game = False
                    continue
                elif display == "1":
                    texto = "Agarras la barca la vuelcas hacia el suelo y la arrastras hasta el agua, una vez allí te fijas que en el interior de la barca hay lo que parece un pequeño saco de monedas. Al comprobar su contenido encuentras 9 monedas de oro."
                    inventario.add(["Saco de monedas"])
                    saco_monedas += 9
      
        elif display == "2":
            display_acercarse_a()           # Con esta función desplegamos las opciones de acercarse a la sirena y al orbe.

             
    return "EXIT_LEVEL"