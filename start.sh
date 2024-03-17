#!/bin/bash

# Activar el entorno virtual
source venv\Scripts\activate.bat

# Ir al directorio del proyecto Django
cd ./MindFlow_BackEnd/MindFlow_BackEnd

# Ejecutar Gunicorn
gunicorn MindFlow_BackEnd.wsgi:application
