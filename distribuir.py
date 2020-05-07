import catalogar

# Esta función crea las subcarpetas con los nombres en base al primer caracter del primero y último ficheros.

def distribuir():
    archivos_por_carpeta = catalogar.total // catalogar.cantidad_de_carpetas
    contador_subcarpeta = 0
    subca = []
    contador = 0

    for i in range(catalogar.cantidad_de_carpetas):
        subca.append("")

    for nombre in sorted(catalogar.archivos, key=str.lower):
        if subca[contador_subcarpeta] == "":
            if contador_subcarpeta == 0:
                subca[contador_subcarpeta] = nombre[0].casefold()
            else:
                # Si no es la primer subcarpeta, empezar con la letra siguiente.
                subca[contador_subcarpeta] = chr(ord(nombre[0].casefold()) + 1)
        contador += 1
        if contador > archivos_por_carpeta:
            subca[contador_subcarpeta] = subca[contador_subcarpeta] + "-" + nombre[0].casefold()
            contador_subcarpeta += 1
            contador = 0
    subca[contador_subcarpeta] = subca[contador_subcarpeta] + "-" + nombre[0].casefold()
    return subca



