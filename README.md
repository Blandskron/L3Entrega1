# L3Entrega1

# Mi Proyecto Django
Este es un proyecto Django que incluye una aplicación para crear formularios con validación en el backend y utiliza el principio DRY (Don't Repeat Yourself) y la herencia de plantillas para mantener el código organizado y reutilizable.

## Pasos para Configurar y Ejecutar el Proyecto
Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

### 1. Clonar el Repositorio
Primero, clona este repositorio en tu máquina local utilizando el siguiente comando:

git clone https://github.com/Blandskron/L3Entrega1.git

### 2. Instalar Dependencias
Ve al directorio raíz del proyecto y crea un entorno virtual. Luego, instala las dependencias del proyecto con el siguiente comando:

pip install -r requirements.txt

### 3. Crear y Aplicar Migraciones
Asegúrate de que tu base de datos esté configurada correctamente en `settings.py`. Luego, ejecuta los siguientes comandos para crear y aplicar las migraciones:

python manage.py makemigrations
python manage.py migrate

### 4. Ejecutar el Servidor de Desarrollo
Inicia el servidor de desarrollo con el siguiente comando:

python manage.py runserver

### 5. Acceder al Sitio Web
Abre tu navegador web y visita `http://127.0.0.1:8000/` para acceder al sitio web.

## Estructura del Proyecto
La estructura del proyecto es la siguiente:

mi_proyecto_django/
│
├── myapp/
│ ├── migrations/
│ ├── templates/
│ │ └── myapp/
│ │ └── nueva_pagina.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
│
├── mi_proyecto_django/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── init.py
│
├── templates/
│ └── base.html
│
├── manage.py
└── README.md

## Acerca de la Aplicación
### Formulario
La aplicación incluye un formulario (`MyForm`) que se puede utilizar para recopilar datos de los usuarios. El formulario utiliza la validación en el backend de Django.

### Plantilla Base
La plantilla `base.html` se utiliza como plantilla base para todas las páginas del sitio. Contiene un encabezado, una barra de navegación y un pie de página.

Para más detalles sobre cómo usar la aplicación y personalizarla según tus necesidades, consulta el código fuente y la documentación dentro de cada archivo.
