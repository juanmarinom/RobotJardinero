# Instalador del entorno virtual

import subprocess

print("""
############# PASO 1
    Se procede a instalar en caso de no estar instalado virtualenv
""")
subprocess.run("pip install virtualenv")
print("""
############# PASO 2
    Se crea un entorno virtual en la carpeta en la que nos encontramos
""")
subprocess.run("virtualenv venv")
print("""
############# PASO 3
    Se accede al entorno virtual y se instalan las librerias necesarias
""")
subprocess.run("venv\\Scripts\\pip install -r requirements.txt",shell=True)
print("""
############# PASO 4
    Se instala tensorflow para la version de python que se esté utilizando
""")

print("############# FIN DE LA INSTALACION")
