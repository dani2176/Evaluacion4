from netmiko import ConnectHandler

# Datos del router Cisco
router = {
    "device_type": "cisco_ios",
    "host": "IP_DEL_ROUTER",
    "username": "USUARIO",
    "password": "CONTRASEÑA",
}

def conectar():
    try:
        conexion = ConnectHandler(**router)
        print("Conexión exitosa al router.")
        return conexion
    except Exception as e:
        print(f"Error al conectar: {e}")
        return None