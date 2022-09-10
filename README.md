# TaskControl
### Started
A- Descarga el repositorio:
   1- Primero crea una carpeta en el escritorio
   2- Abre "git bash" o "cmd" y cambiate al escritorio
   3- En windows usa el comando "dir" para ver directorios, y "ls" en linux
   4- Busca el escritorio (Desktop) y cambiate a el con el comando "cd Desktop"
   5- una vez en el escritorio cambiate a la carpeta creada: "cd <nombre-carpeta>"
   6- dentro de la carpeta copia el repostorio con el comando: 
      "git clone https://github.com/carloslun/TaskControl.git"

B- Crear un ambiente virtual
   1- Abre el "git bash" o "cmd"
   2- Ejecuta el comando "python -m venv venv" para windows
      "python3 -m venv venv" para otro sistema
      Esto creará el ambiente
   3- Para activar el ambiente se usa el comando "source venv/Scripts/activate"
      para windows
      "source venv/bin/activate" para otro sistema

C- Instala Django
   1- Abre el "git bash" o "cmd"
   2- Ejecuta el comando "pip install django"

D- Instala RestFramework
   1- Abre el "git bash" o "cmd"
   2- Ejecuta el comando "pip install djangorestframework"

E- Entrar al proyecto
   1- Abre el "git bash" o "cmd"
   2- Ve al escritorio usando el "git bash" o "cmd"
   3- Entra en la carpeta del proyecto con "cd <nombre-carpeta>"
   4- Una vez dentro del proyecto, entra a la carpeta core con "cd core"
   5- Ejecuta "python manage.py runserver" para iniciar el proyecto en windows
      "python3 manage.py runserver" para otro sistema
