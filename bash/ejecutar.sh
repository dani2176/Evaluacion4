#!/bin/bash

echo "====================================="
echo " INICIO DE LA AUTOMATIZACIÓN"
echo "====================================="

echo ""
echo "1. Ejecutando Playbook de Ansible..."
cd ~/Evaluacion4/ansible
ansible-playbook playbook_base.yml

echo ""
echo "2. Validando configuración..."
cd ~/Evaluacion4/python
python3 validar_red.py

echo ""
echo "3. Generando reporte..."
python3 reporte.py

echo ""
echo "4. Generando backup..."
python3 backup.py

echo ""
echo "====================================="
echo " PROCESO FINALIZADO"
echo "====================================="