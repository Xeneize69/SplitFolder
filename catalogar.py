""" Versión 2.0

        No almacena cantidad de archivos que comienzan con cada caracter.
        Cada subcarpeta se denomina con los x primeros caracteres del 
        primer archivo y los x primeros del último.
"""

import os

cantidad_de_carpetas = 0

def catalogar(basepath):
    archivos = []
    subcarpeta = []
    global cantidad_de_carpetas

    for dirpath, dirnames, files in os.walk(basepath):
        for carp in dirnames:
            subcarpeta.append(carp)
            cantidad_de_carpetas += 1
        for file_name in files:
            archivos.append(file_name)
    return archivos

# Versión más moderna, pero extremadamente lenta.

def catalogar2(directorio):
    global archivos, cantidad_de_carpetas

    p = Path(directorio)
    for nombre in p.iterdir():
        if nombre.is_dir():
            cantidad_de_carpetas += 1
            catalogar2(nombre)
        if nombre.is_file():
            archivos.append(PurePath(nombre).name)
