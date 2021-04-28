
import time,sys

# Esta funcion sirve para imprimir texto con un efecto de tipado.
def escribe_texto(txt):

    texto = txt.split()
    for palabra in texto:
        palabra += " "
    
        for letra in palabra:
            # si el carácter es diferente a un punto o existen puntos supensivos, se printean las letras una seguida de otras
            if letra != "." or "..." in palabra:
                print(letra, end='') 
                # sys.stdout.flush() Borra el bufer permitiendo no tener que esperar a que se ejecute todo el timpo de espera.
                sys.stdout.flush() 
                time.sleep(0.02) 
            else:
                print(letra)
                sys.stdout.flush()
                time.sleep(0.02)



historia = ["Esta habitación parece sacada de una película de Sherlock Holmes.A primera vista puedo ver un escritorio justo enfrente, y estanterias con libros llenos de polvo a los lados.Me pregunto si podré encontrar algo de utilidad en esta habitación... ","Esta habitación asdfsdafdsafsde una película de Sherlock Holmes.A primera vista puedo ver un escritorio justo enfrente, y estanterias con libros llenos de polvo a los lados.Me pregunto sadfsdafdsj sdjhaskjhasd asdfsad abitación... "]
escribe_texto(historia)
