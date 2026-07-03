from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.103",
    "username": "cisco",
    "password": "cisco123",
    "secret": "cisco123",
    "port": 22,
    "fast_cli": False,
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