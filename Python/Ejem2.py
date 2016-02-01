# Ejemplo de expresiones regulares

import re

str = "un ejemplo de palabra:cat!!"
match = re.search(r'palabra:\w\w\w', str)
if match:
        print('Encontramos la', match.group())
else:
        print('la palabra no encontrada')
