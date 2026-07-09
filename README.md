# ⚡ Automatización de Redes con Ansible

Automatización de la configuración de dispositivos Cisco IOS mediante Ansible utilizando un servidor Ubuntu Server, acceso remoto con Visual Studio Code Remote SSH y conectividad segura mediante ZeroTier.

---

# 📌 Descripción del Proyecto

Este proyecto consiste en la automatización de tareas de administración de redes Cisco utilizando Ansible como herramienta de gestión de configuraciones.

El entorno fue implementado sobre un servidor Ubuntu Server que actúa como nodo de control (Control Node), desde donde se ejecutan playbooks para administrar un router Cisco IOS mediante el protocolo SSH.

El desarrollo fue realizado de forma colaborativa entre dos integrantes ubicados en diferentes sitios, utilizando ZeroTier para establecer una VPN privada y Visual Studio Code Remote SSH para trabajar simultáneamente sobre el mismo servidor.

---

# 🎯 Objetivos del Proyecto

Automatizar la configuración de dispositivos Cisco IOS para:

- Reducir errores de configuración.
- Estandarizar despliegues.
- Facilitar la administración remota.
- Implementar Infraestructura como Código (IaC).
- Mejorar el trabajo colaborativo mediante acceso remoto.

---

# 🚀 Tecnologías Utilizadas

- Ubuntu Server 22.04 LTS
- Ansible
- Python 3
- Cisco IOS
- OpenSSH Server
- Visual Studio Code
- Remote SSH Extension
- ZeroTier One
- Git
- GitHub
- YAML

---

# 🧠 Funcionalidades Implementadas

Actualmente el proyecto permite:

### Administración de Equipos Cisco

- Configuración automática de interfaces.
- Configuración de direcciones IP.
- Configuración de VLAN.
- Configuración de SSH.
- Ejecución remota de comandos.
- Automatización mediante Playbooks.

### Administración del Servidor

- Gestión remota mediante SSH.
- Ejecución de Ansible.
- Organización de inventarios.
- Gestión de configuraciones.

### Trabajo Colaborativo

- Acceso simultáneo mediante VS Code.
- Conectividad privada mediante ZeroTier.
- Administración remota del servidor Ubuntu.

---

# 📡 Arquitectura del Proyecto

```text
                     Internet
                         │
                  ZeroTier VPN
                         │
        ┌──────────────────────────────────┐
        │                                  │
  Integrante 1                      Integrante 2
 Visual Studio Code               Visual Studio Code
     Remote SSH                     Remote SSH
        │                                  │
        └────────────── SSH ───────────────┘
                         │
                  Ubuntu Server
                  (Control Node)
                         │
                      Ansible
                         │
                     SSH (Puerto 22)
                         │
                 Router Cisco IOS
```

---

# 📂 Estructura del Proyecto

```text
Evaluacion4/
│
├── ansible/
│   ├── ansible.cfg
│   ├── inventory.ini
│   ├── playbook_interfaces.yml
│   ├── playbook_base.yml
│   └── host_vars/
│
├── evidencias/
│
├── README.md
│
└── docs/
```

---

# ⚙️ Requisitos

## Software

- Ubuntu Server 22.04
- Python 3
- Ansible
- OpenSSH Server
- Cisco IOS
- Visual Studio Code
- Remote SSH Extension
- ZeroTier One

---

# 📋 Instalación

## Actualizar Ubuntu

```bash
sudo apt update
sudo apt upgrade -y
```

---

## Instalar Ansible

```bash
sudo apt install ansible -y
```

Verificar instalación

```bash
ansible --version
```

---

## Instalar colección Cisco IOS

```bash
ansible-galaxy collection install cisco.ios
```

Verificar

```bash
ansible-galaxy collection list
```

---

# 🔐 Configuración SSH

Verificar que el servicio SSH esté activo

```bash
sudo systemctl status ssh
```

Reiniciar servicio

```bash
sudo systemctl restart ssh
```

Verificar conectividad

```bash
ssh usuario@IP_DEL_SERVIDOR
```

---

# 🌐 Configuración ZeroTier

1. Instalar ZeroTier.
2. Unirse a la red privada.
3. Autorizar el dispositivo desde ZeroTier Central.
4. Verificar la IP asignada.

Comprobar interfaz

```bash
ip a
```

---

# 📂 Configuración del Inventario

Ejemplo de `inventory.ini`

```ini
[cisco]

Router1 ansible_host=192.168.10.1

[cisco:vars]

ansible_user=cisco
ansible_password=cisco123
ansible_connection=network_cli
ansible_network_os=cisco.ios.ios
ansible_port=22
```

---

# 🚀 Ejecución de Playbooks

Verificar sintaxis

```bash
ansible-playbook playbook_interfaces.yml --syntax-check
```

Ejecutar playbook

```bash
ansible-playbook playbook_interfaces.yml
```

---

# ✔️ Verificaciones

Comprobar conexión

```bash
ansible cisco -m ping
```

Mostrar versión IOS

```bash
ansible Router1 -m cisco.ios.ios_command -a "commands='show version'"
```

Mostrar interfaces

```bash
ansible Router1 -m cisco.ios.ios_command -a "commands='show ip interface brief'"
```

Mostrar configuración

```bash
ansible Router1 -m cisco.ios.ios_command -a "commands='show running-config'"
```

---

# 💻 Trabajo Colaborativo

El proyecto fue desarrollado por dos integrantes ubicados en diferentes lugares.

## Integrante 1

Responsabilidades:

- Instalación de Ubuntu Server.
- Configuración de Ansible.
- Configuración del Router Cisco.
- Desarrollo de Playbooks.

## Integrante 2

Responsabilidades:

- Instalación de Visual Studio Code.
- Configuración Remote SSH.
- Configuración ZeroTier.
- Pruebas de funcionamiento.
- Documentación del proyecto.

---

# 📷 Evidencias

Durante el desarrollo se documentó mediante capturas de pantalla:

- Instalación de Ubuntu Server.
- Configuración de ZeroTier.
- Dirección IP del servidor.
- Conexión Remote SSH.
- Instalación de Ansible.
- Inventario de dispositivos.
- Ejecución de Ansible Ping.
- Ejecución de Playbooks.
- Configuración aplicada al Router Cisco.
- Verificación mediante comandos IOS.

---

# 📋 Comandos Utilizados

Actualizar sistema

```bash
sudo apt update
```

Mostrar IP

```bash
ip a
```

Ver rutas

```bash
ip route
```

Estado SSH

```bash
sudo systemctl status ssh
```

Probar conectividad

```bash
ping 192.168.10.1
```

Ingresar al router

```bash
ssh cisco@192.168.10.1
```

---

# 📁 Archivos Principales

| Archivo | Descripción |
|----------|-------------|
| ansible.cfg | Configuración de Ansible |
| inventory.ini | Inventario de dispositivos |
| playbook_interfaces.yml | Automatización de interfaces |
| playbook_base.yml | Configuración base |
| README.md | Documentación del proyecto |
| evidencias/ | Capturas del desarrollo |

---

# 🔄 Flujo de Trabajo

1. Iniciar Ubuntu Server.
2. Conectar ZeroTier.
3. Acceder mediante Remote SSH.
4. Abrir el proyecto en VS Code.
5. Ejecutar los playbooks.
6. Verificar la configuración aplicada.
7. Documentar los resultados.

---

# 📌 Estado Actual del Proyecto

## Funcionalidades Implementadas

- Instalación de Ubuntu Server.
- Configuración de SSH.
- Configuración de ZeroTier.
- Instalación de Ansible.
- Configuración del inventario.
- Automatización mediante Playbooks.
- Administración remota del Router Cisco.
- Trabajo colaborativo mediante VS Code Remote SSH.
- Documentación del proyecto.

---

# 📈 Resultados Obtenidos

- Comunicación exitosa entre Ubuntu Server y Cisco IOS mediante SSH.
- Automatización de configuraciones utilizando Ansible.
- Ejecución remota de comandos IOS.
- Administración colaborativa desde diferentes ubicaciones mediante ZeroTier.
- Implementación de un entorno funcional para automatización de redes.

---

# 👨‍💻 Autores

- **Daniel Videla**
- **Nicolás Bastidas**

---

# 📄 Licencia

Este proyecto fue desarrollado con fines académicos para la asignatura de Automatización de Redes.
