import re

# Pre-compilamos el patron del texto

regexes = [re.compile(p) for p in ['sc',
                                    'py']
                                    ]
texto = "Scala y python son lenguajes de programacion?"

for regex in regexes:
        print('Buscando por "%s" en "%s" ->' %(regex.pattern, texto),)
        if regex.search(texto):
                print('Encontramos un emparejamiento')
        else:
                print('No hay emparejamientos')
