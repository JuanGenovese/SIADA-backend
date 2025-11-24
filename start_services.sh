#!/bin/bash

export PYTHONPATH=$(pwd)
if [ -f .venv/bin/activate ]; then
    source .venv/bin/activate
    echo "Activando entorno virtual en .venv"
else 
    source venv/Scripts/activate
    echo "Activando entorno virtual en venv"
fi

echo "Iniciando las API en el puerto 8000..."
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload &

wait
