import os

# empieza_con = []
# cantidad_por_letra = []
cantidad_de_carpetas = 0

def catalogar(basepath):
    # indice = -1
    archivos = []
    subcarpeta = []
    global cantidad_de_carpetas
    # global cantidad_por_letra, empieza_con

    for dirpath, dirnames, files in os.walk(basepath):
        for carp in dirnames:
            subcarpeta.append(carp)
            cantidad_de_carpetas += 1
        for file_name in files:
            # Chequear si la letra inicial cambió (mayúsculas = minúsculas)
        # if not empieza_con or empieza_con[indice].casefold() \
        #          != file_name[0].casefold():
        #    indice += 1
        #     cantidad_por_letra.append(0)
        #    empieza_con.append(file_name[0])
            archivos.append(file_name)
    #            cantidad_por_letra[indice] += 1
    # try:
    #    f = open("Siloplist.txt", "w")
    #    l1 = map(lambda x:x+"\n", archivos)
    #    f.writelines(l1)
    #    f.close()
    # except:
    #    pass
    return archivos

def catalogar2(directorio):
    global archivos, cantidad_de_carpetas

    p = Path(directorio)
    for nombre in p.iterdir():
        if nombre.is_dir():
            cantidad_de_carpetas += 1
            catalogar2(nombre)
        if nombre.is_file():
            archivos.append(PurePath(nombre).name)