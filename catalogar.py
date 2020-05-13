""" Versión 2.0

        No almacena cantidad de archivos que comienzan con cada caracter.
        Cada subcarpeta se denomina con los x primeros caracteres del 
        primer archivo y los x primeros del último.
"""

import os

def catalogar(basepath):
    """" Obtiene todos los archivos de una carpeta y de sus subcarpetas.
         Argumentos: Carpeta().ruta
         Retorna: String archivos[] """
    archivos = []

    for dirpath, dirnames, files in os.walk(basepath):
        for file_name in files:
            archivos.append(file_name)
    return archivos
