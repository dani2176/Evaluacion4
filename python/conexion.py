from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.10.1",
    "username": "cisco",
    "password": "cisco123",
}

def conectar():
    try:
        conexion = ConnectHandler(**router)
        conexion.enable()
        print("Conexión exitosa.")
        return conexion

    except Exception as e:
        print(type(e))
        print(e)
        return None