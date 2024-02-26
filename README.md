# Market Web App

## Descripción
Market es una aplicación web desarrollada en Python utilizando el framework Flask. Esta aplicación permite a los usuarios realizar operaciones relacionadas con compras, ventas y gestión de productos.


### Arquitectura de Capas

La arquitectura de capas es un patrón común en el desarrollo de software que organiza el código en distintas capas o niveles, cada una con una responsabilidad específica.

1. **Capa de Presentación (Routes y Templates):** Esta capa maneja la interacción con el cliente. Los archivos en la carpeta `routes` contienen la lógica de enrutamiento de Flask, donde se definen las rutas y las funciones de vista que manejan las solicitudes HTTP y renderizan las plantillas HTML ubicadas en la carpeta `templates`.

2. **Capa de Servicio (Services):** Esta capa proporciona la lógica de negocio de la aplicación. Los servicios son componentes que encapsulan la funcionalidad de la aplicación y proporcionan una interfaz coherente para interactuar con ella. Los archivos en la carpeta `services` contienen la implementación de estos servicios, como lógica de autenticación, procesamiento de datos, validación, etc.

3. **Capa de Acceso a Datos (Repositories y Models):** Esta capa se encarga de interactuar con la base de datos y manejar la persistencia de datos. Los archivos en la carpeta `repositories` contienen la lógica para interactuar con la base de datos, como consultas y operaciones CRUD. La carpeta `models` contiene las definiciones de los modelos de datos utilizados en la aplicación, que representan las entidades y relaciones en la base de datos.


### Librerías Utilizadas

1. **Flask-PyMongo:** Esta librería proporciona integración entre Flask y MongoDB, permitiendo interactuar fácilmente con una base de datos MongoDB desde una aplicación Flask.

2. **Flask-Login:** Flask-Login proporciona herramientas para la gestión de sesiones de usuarios, autenticación y autorización en aplicaciones Flask. Facilita la gestión de la autenticación de usuarios y el acceso a rutas protegidas.

3. **Redis:** Redis es una base de datos en memoria de código abierto que se utiliza comúnmente para caché, almacenamiento en caché y como almacenamiento de datos en tiempo real. En el contexto de tu aplicación, Redis se utiliza para la caché, lo que significa que puede almacenar temporalmente resultados de consultas o datos frecuentemente accedidos en memoria, lo que puede mejorar el rendimiento de la aplicación al reducir los tiempos de acceso a la base de datos principal.

## Configuración

Antes de ejecutar la aplicación, asegúrate de tener instalado Python y las bibliotecas requeridas. Puedes instalar las dependencias utilizando el siguiente comando:

```
pip install -r requirements.txt
```


## Ejecución

Para ejecutar la aplicación, simplemente ejecuta el archivo `app.py` desde la línea de comandos:

```
python src/app.py
```


Esto iniciará el servidor Flask y podrás acceder a la aplicación desde tu navegador web visitando `http://localhost:3000`.



### Propuesta

#### Elección de una Base Documental y Caché

Para esta aplicación, hemos optado por utilizar una base de datos documental y una caché por las siguientes razones:

1. **Base Documental (MongoDB):** Elegimos una base documental, como MongoDB, debido a su capacidad para almacenar y consultar información semiestructurada sin la necesidad de una estructura definida. Esto nos brinda un modelo flexible que puede manejar numerosos tipos de datos, lo que simplifica las tareas de adición y actualización de datos. Además, MongoDB es altamente escalable y ofrece una gran velocidad de lectura y escritura, lo que lo hace ideal para aplicaciones web que manejan una cantidad variable de datos. Las colecciones que hemos creado en MongoDB para esta aplicación son:
   - **usuario**
   - **producto**
   - **pedido**
   - **factura**

2. **Caché (Redis):** Para el feature de carrito de compras, tenemos un requerimiento de modificación constante del carrito, donde los usuarios pueden agregar, eliminar o modificar elementos del carrito en tiempo real. Para manejar esta funcionalidad de manera eficiente, utilizamos Redis como caché. Redis es una base de datos en memoria que ofrece una gran velocidad de acceso y es ideal para almacenar datos temporales que necesitan ser accedidos rápidamente. Decidimos utilizar Redis con una estructura de datos JSON, donde la clave (key) es el nombre de usuario y el valor (value) es un objeto JSON que contiene la información del usuario, los productos en el carrito, el monto total y la cantidad de productos. Esto nos permite almacenar y recuperar fácilmente la información del carrito de compras de cada usuario de manera eficiente.

