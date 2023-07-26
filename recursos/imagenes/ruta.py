import os 


def ruta_imagenes(objecto):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    # print(directorio_actual)

    return f"'{directorio_actual}/{objecto}'"

if __name__ == "__main__":
   ruta = ruta_imagenes("Run1.jpg")
   print(ruta)
