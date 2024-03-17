#!/bin/bash

# Activar el entorno virtual
source source ./venv/Scripts/activate

# Ir al directorio del proyecto Django
cd ./MindFlow_BackEnd/MindFlow_BackEnd

# Ejecutar Gunicorn
gunicorn MindFlow_BackEnd.wsgi:application