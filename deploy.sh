#1/bin/bash
echo  'Inicaindo el despliegue automatico de Don Alberto'
# Moverse a la carpeta
cd /home/$USER/moto/api
#Traer los cambios desde git
echo 'Trayendo la ultima version desde git'
git pull origin master 
#Activar el entorno virtual 
echo 'asegurando las dependencias'
source venv/bin/activate
pip install -r requeriments.txt --quiet
# reiniciar el servidor de systemd
echo 'Reiniciado el motor gunicorn'
sudo sysytemctl restart gigamoto.service
#verificar que este vivo
echo 'despliegue completado con exito. El estado actual es:'
sudo systemctl status gigamoto.service | grep 'Active:'

