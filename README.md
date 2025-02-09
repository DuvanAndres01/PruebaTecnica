# Backend E-commerce

# Descripción 

El backend de TiendaPC es una API RESTful desarrollada en **Django** y **Django REST Framework** que proporciona los siguientes servicios:

- Gestión de productos (crear, leer, actualizar, eliminar).
- Autenticación de usuarios.
- Interacción con la base de datos PostgreSql

# Requisitos 

Antes de ejecutar el backend, asegúrate de tener instalado lo siguiente:

- **Python** (v3.8 o superior)
- **pip** (v20 o superior)
- **Django** (v4.0 o superior)
- **Django REST Framework** (v3.14 o superior)

# Estructura del proyecto 

backend/
├── manage.py              # Script para gestionar el proyecto Django
├── db.sqlite3             # Base de datos SQLite
├── requirements.txt       # Dependencias del proyecto
├── backend/
│   ├── __init__.py        # Archivo que indica que es un paquete Python
│   ├── settings.py        # Configuración del proyecto Django
│   ├── urls.py            # Rutas principales del proyecto
│   ├── wsgi.py            # Configuración WSGI para despliegue
api/
    ├── __init__.py        # Archivo que indica que es un paquete Python
    ├── models.py          # Modelos de la base de datos
    ├── views.py           # Vistas de la API
    ├── serializers.py     # Serializadores para los modelos
    ├── urls.py            # Rutas de la API
    ├── admin.py           # Configuración del panel de administración
    ├── tests.py           # Pruebas unitarias


