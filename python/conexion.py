from netmiko import ConnectHandler

# Datos del router Cisco
router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.103",
    "username": "cisco",
    "password": "cisco123",
}

def conectar():
    try:
        conexion = ConnectHandler(**router)
        print("Conexión exitosa al router.")
        return conexion
    except Exception as e:
        print(f"Error al conectar: {e}")
        return None