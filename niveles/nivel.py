##########################################################
from pathlib import Path
import sys

url = (str(Path(__file__).parent.absolute())).split("\\")
url.pop(-1)
url = "\\".join(url)

sys.path.append(url)

from modulos.display import display
##########################################################
texto = "asdasfsdafdsafsdjak gsadgfsad sdfajfasd lasdgads ldfasga sfdasdg fdsalgf asdasd flasdg dasgf asdlsdgaf askdjf asdgf ds"
opciones = ['salir', 'pegar a Jandro', 'pegar a Javi', 'pegar a Alberto']


if display(texto,opciones) == 0:
    print("adios")
else:
    print("saas")
