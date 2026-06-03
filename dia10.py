# DIA 10 - LECTURA SEGURA DE ARCHIVOS


with open("usuario.txt", "w") as archivo:

 archivo.write("Ana, 25\n")
 archivo.write("Luis, 30\n")
 archivo.write("Marta, 22\n")
print("Archivo creado correctamente")

try:
    with open("usuario.txt", "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo no existe.")
except Exception as e:
   print(f"Error inesperado: {e}")

print("programa termino, El archivo se cerro solo.")

with open("log.txt", "w") as f:
   f.write("Sebastian Botero - 2026-06-02")
           
