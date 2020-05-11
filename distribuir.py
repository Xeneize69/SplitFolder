CANT_CARPETAS = 4
LONG_NOMBRE = 6

def distribuir(archivos):

    archivos_por_carpeta = len(archivos) // CANT_CARPETAS
    cont_subc = 0
    contador = 0
    subca = [""] * CANT_CARPETAS

    archivos.sort(key=str.lower)

    for nombre in archivos:
        if subca[cont_subc] == "":
            if cont_subc == 0:
                subca[cont_subc] = nombre[0].casefold()
            else:
                subca[cont_subc] = chr(ord(nombre[0].casefold()) + 1)
        contador += 1
        if contador > archivos_por_carpeta:
            subca[cont_subc] += "-" + nombre[0].casefold()
            cont_subc += 1
            contador = 0
    subca[cont_subc] += "-" + nombre[0].casefold()
    return subca

def distribuir2(archivos):

    archivos_por_carpeta = len(archivos) // CANT_CARPETAS
    cont_subc = 0
    contador = 0
    subca = [""] * CANT_CARPETAS

    archivos.sort(key=str.lower)

    for nombre in archivos:
        if subca[cont_subc] == "":
            if cont_subc > 0 and subca[cont_subc-1][-LONG_NOMBRE:] \
                    == nombre[:LONG_NOMBRE]:
                subca[cont_subc] = nombre[:LONG_NOMBRE+1]
            else:
                subca[cont_subc] = nombre[:LONG_NOMBRE]
        contador += 1
        if cont_subc < CANT_CARPETAS - 1 and \
                contador > archivos_por_carpeta:
            subca[cont_subc] += "-" + nombre[:LONG_NOMBRE]
            cont_subc += 1
            contador = 0
    subca[cont_subc] += "-" + nombre[:LONG_NOMBRE]
    return(subca)