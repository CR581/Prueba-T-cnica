- Python 3.8 o superior
- Node.js y npm (para el frontend)
- Redis (para la cola de tareas con Celery)
- Django
- Django REST Framework
- Celery
- Redis Python Client

Paso a paso:

- Clona y descarga el código que se encuentra en el repositorio.
- Extrae y abre el proyecto en Visual Studio Code.
- Instala las dependencias de Python.
- Crea un entorno virtual y actívalo: python -m venv venv y .\venv\Scripts\Activate.
- Instala las dependencias del backend: pip install -r requirements.txt.
- Restaura la base de datos ejecutando el siguiente comando: cp db.sqlite3.backup db.sqlite3.
- Aplica las migraciones en caso de ser necesario: python manage.py migrate.
- Ejecuta el servidor de Django con python manage.py runserver.
- Abre una nueva terminal y navega a la carpeta del frontend prueba_django_react.
I- nstala las dependencias del frontend con npm install.
- Ejecuta el servidor de React con npm start.
- Al ejecutarse y mostrar el login en la página, ingresa la siguiente información: "correo: y@gmail.com" y "#Documento: 2222". Si el documento o el correo no coinciden con los de la base de datos, el sistema mostrará un mensaje de error.
- Al iniciar sesión, el sistema mostrará un mensaje de éxito y te dirigirá a una pantalla con todos los usuarios registrados. En esta pantalla, también se pueden ver dos botones: "Crear usuario" y "Cerrar sesión".
- Al presionar el botón "Cerrar sesión", el sistema redirigirá al usuario nuevamente a la pantalla de login.
- Al presionar el botón "Crear usuario", el sistema redirigirá al usuario a una pantalla con un formulario para registrar nuevos usuarios.
- Para descargar automáticamente el documento del DANE, abre una nueva terminal y ejecuta el siguiente comando: python documents/scripts/download_document.py. Al ejecutarlo, se descargará el documento del DANE y se guardará en una carpeta llamada "Media" dentro del módulo documents.
- Para que el archivo se actualice periódicamente, descarga Redis y configúralo en las variables de entorno.
- Después de tener Redis configurado, abre una nueva terminal y ejecuta el siguiente comando: redis-server.
- Luego, en una nueva terminal, ejecuta el comando: celery -A Prueba_django_api worker --loglevel=info (nota: el entorno virtual debe estar activo).
- En una nueva terminal, ejecuta el comando: celery -A Prueba_django_api beat --loglevel=info (nota: el entorno virtual debe estar activo).
- Si todo está correcto, en la consola donde se ejecutó el worker se mostrará el mensaje: "Documento guardado en ...".
(Nota: En estos momentos esta configurado para que se actualice cada 3 horas)
  
  
  
