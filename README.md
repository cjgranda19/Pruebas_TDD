#1. instalamos la variable de entorno
python -m venv venv
#2. Activamos el entorno
.\venv\Scripts\Activate.ps1
#3. Instalar pytest dentro del virtualenv
pip install pytest
#4. Ejecutamos los test
python -m pytest -q
