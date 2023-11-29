# Tercera_Preentrega_Muñoz -- CoderHouse Python 47785

Este es un blog donde se podra agregar autores y buscar dentro de la BD, ademas de ver los post que se han agregado y los comentarios. 

El principal objetivo de este proyecto fue el crear una WEB Django con patron MVT, con las siguientes características:
* Herencia HTML
* Minimo 3 clases en models
* Un formulario para insertar datos a las clases del models
* Un formulario para buscar en la BD

## Instalación
1. **Clonar el Repositorio:**

https://github.com/cyngms/Tercera-pre-entrega-Mu-oz.git

2. **Crear un entorno virtual**
    
   `python -m venv venv`

3. **Instalar Django**

    `pip install django`
4. **En caso de ser necesario, actualice Django**

    `python.exe -m pip install --upgrade pip`

## Configuración
**Aplica las migraciones**
    `python manage.py makemigrations`

**Ejecutar el manage.py, para visulizar la URL** 
    `python manage.py runserver`

Visite la URL en su navegador, que se le proporcionó en la consola

# Estructura del Proyecto

* 'manager': Carpeta que contiene las aplicaciones 
* 'core/': Carpeta de la aplicación Django
* 'templates': Plantilla base HTML
* 'templates/core': Plantillas de los forms y views HTML 
