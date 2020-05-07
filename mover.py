import shutil
import os
import catalogar

def mover(subcarpetas):
    basepath = "C:/Users/hgazz/Downloads/Silop"
    for i in subcarpetas:
        try:
            os.mkdir(os.path.join(basepath, i))
        except FileExistsError as exc:
            pass

    for dirpath, dirnames, files in os.walk(catalogar.basepath):
        for names in files:
            if not os.path.isfile(os.path.join(dirpath, names)):
                continue
            inicial = names[0].casefold()
            for carp in subcarpetas:
                if inicial >= carp[0] and inicial <= carp[2]:
                    dest = os.path.join(basepath, carp, names)
                    orig = os.path.join(dirpath, names)
                    if not os.path.isfile(dest):
                        try:
                            shutil.copy(orig, dest)
                            break
                        except:
                            print(orig, dest)
                            raise

