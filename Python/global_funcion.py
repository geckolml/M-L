# uso de la funcion globals() en el uso de modulos

import  math
import textwrap

x = math.sqrt(5)

def f1():
    pass

gl = globals()
gb = ' ,'.join(gl)

print (textwrap.fill(gb))