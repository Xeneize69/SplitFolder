import os

archivos = []
empieza_con = []
cantidad_por_letra = []
cantidad_de_carpetas = 0
basepath = "P:/Silop"
total = 0

def catalogar():
    indice = -1
    subcarpeta = []
    global archivos, empieza_con, cantidad_de_carpetas, cantidad_por_letra, basepath, total, empieza_con

    for dirpath, dirnames, files in os.walk(basepath):
        for carp in dirnames:
            subcarpeta.append(carp)
            cantidad_de_carpetas += 1
        total += len(files)
        for file_name in sorted(files, key=str.lower):
            # Chequear si la letra inicial cambió (mayúsculas = minúsculas)
            if not empieza_con or empieza_con[indice].casefold() != file_name[0].casefold():
                indice += 1
                cantidad_por_letra.append(0)
                empieza_con.append(file_name[0])
            archivos.append(file_name)
            cantidad_por_letra[indice] += 1