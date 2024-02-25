# Market

Este repositorio contiene el código fuente de una aplicación web desarrollada con Flask, una biblioteca de Python para construir aplicaciones web. La aplicación está diseñada siguiendo una arquitectura basada en capas para una mejor organización y mantenibilidad del código.

## Arquitectura

La aplicación sigue una arquitectura basada en capas, donde cada capa tiene una responsabilidad específica:

- **Capa de Presentación:** Encargada de presentar la interfaz de usuario al usuario final. En una aplicación web Flask, esto se logra mediante las vistas y plantillas HTML ubicadas en la carpeta `app/templates`.

- **Capa de Lógica de Aplicación:** Contiene la lógica de negocio de la aplicación, incluyendo la manipulación de datos y el procesamiento de solicitudes del usuario. En nuestra aplicación, esta capa está representada por las rutas y funciones definidas en `app/routes.py`.

- **Capa de Acceso a Datos:** Responsable de interactuar con la base de datos y otros sistemas de almacenamiento de datos. Hemos implementado esta capa utilizando repositorios separados para MongoDB y Redis, ubicados en la carpeta `app/repositories`.

Esta estructura proporciona una separación clara de las preocupaciones y facilita el mantenimiento y la evolución de la aplicación a medida que crece.

## Configuración

Antes de ejecutar la aplicación, asegúrate de tener instalado Python y las bibliotecas requeridas. Puedes instalar las dependencias utilizando el siguiente comando:

```
pip install -r requirements.txt
```


## Ejecución

Para ejecutar la aplicación, simplemente ejecuta el archivo `run.py` desde la línea de comandos:

```
python run.py
```


Esto iniciará el servidor Flask y podrás acceder a la aplicación desde tu navegador web visitando `http://localhost:3000`.


