import json
from conexion import conectar

conexion = conectar()

if conexion:

    datos = {
        "hostname": conexion.send_command("show running-config | include hostname"),
        "interfaces": conexion.send_command("show ip interface brief"),
        "ssh": conexion.send_command("show ip ssh"),
        "ntp": conexion.send_command("show ntp status"),
        "usuarios": conexion.send_command("show running-config | include username")
    }

    with open("../reportes/reporte.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    print("Reporte generado correctamente.")

    conexion.disconnect()