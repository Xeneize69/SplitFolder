import catalogar
import distribuir
import mover
from pathlib import Path, PurePath

class Carpeta:
    """ Estructura básica de una carpeta """

    def __init__(self, path):
        self.ruta = PurePath(path)

    def existe(self):
        return self.ruta.is_dir()

class Subcarpeta(Carpeta):
    """ Extiende Carpeta con funciones propias de las subcarpetas """

    def from_file(self):    # Obtiene la cadena previa a "-" en subcarpetas
        nombre = self.filename()
        divisor = nombre.find("-")
        if divisor == -1:
            return None
        else:
            return nombre[:divisor]

    def to_file(self):      # Obtiene la cadena posterior a "-" en subcarpetas
        nombre = self.filename()
        divisor = nombre.find("-")
        if divisor == -1:
            return None
        else:
            return nombre[divisor:]

def main():
    pCloud = (Carpeta("P:/Silop"))
    archivos = catalogar.catalogar(pCloud)
    #mover.mover(basepath, distribuir.distribuir2)
    print(distribuir.distribuir2(archivos))

if __name__ == "__main__":
    main()