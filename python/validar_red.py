from conexion import conectar

conexion = conectar()

if conexion:

    hostname = conexion.send_command("show running-config | include hostname")
    interfaces = conexion.send_command("show ip interface brief")
    ssh = conexion.send_command("show ip ssh")
    ntp = conexion.send_command("show ntp status")
    usuarios = conexion.send_command("show running-config | include username")

    print("===== HOSTNAME =====")
    print(hostname)

    print("\n===== INTERFACES =====")
    print(interfaces)

    print("\n===== SSH =====")
    print(ssh)

    print("\n===== NTP =====")
    print(ntp)

    print("\n===== USUARIOS =====")
    print(usuarios)

    conexion.disconnect()