# Pokédexter
> Repositorio para practicar django.

# Configuración de compilación
## Crear entorno virtual fuera de la carpeta
``` bash
# 1-) crear entorno virtual ("env" es el nombre este puede ser reemplazado por cualquiera)
python -m venv env

# 2-)Activar el entorno para trabajar
env\Scripts\activate

# Instalar requerimientos 
pip install -r requirements.txt
```

# Comandos utiles 

## Iniciar api
python manage.py runserver

## Crear superuser
python manage.py createsuperuser

## Migraciones 
python manage.py makemigrations

python manage.py migrate

## Migrar datos
python manage.py dumpdata > db.json

python manage.py loaddata db.json

## Para saber que esta instalado en entorno virtual
pip freeze --local

## Inspecciona la base de datos y coloca las tablas en models.py
``` bash
# No utilizar esto comando nuevamente, ya que puede causar errores
```
python manage.py inspectdb > .\app\models.py

## Crear app
python manage.py startapp "nombre"
