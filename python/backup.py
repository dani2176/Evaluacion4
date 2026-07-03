from conexion import conectar
from datetime import datetime

conexion = conectar()

if conexion:

    configuracion = conexion.send_command(
        "show running-config",
        read_timeout=60
    )

    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    nombre_archivo = f"../backups/backup_{fecha}.txt"

    with open(nombre_archivo, "w") as archivo:
        archivo.write(configuracion)

    print(f"Backup guardado en: {nombre_archivo}")

    conexion.disconnect()