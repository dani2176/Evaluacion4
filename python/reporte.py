from conexion import conectar

conexion = conectar()

if conexion:

    print("\n===== HOSTNAME =====")
    print(conexion.send_command("show running-config | include hostname"))

    print("\n===== INTERFACES =====")
    print(conexion.send_command("show ip interface brief"))

    print("\n===== SSH =====")
    print(conexion.send_command("show ip ssh"))

    print("\n===== NTP =====")
    print(conexion.send_command("show ntp status"))

    print("\n===== USUARIOS =====")
    print(conexion.send_command("show running-config | include username"))

    conexion.disconnect()