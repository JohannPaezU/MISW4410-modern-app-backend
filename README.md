# RECIPE BOOK API

📄 Esta carpeta contiene el código fuente para el backend de RECIPE BOOK API. El proyecto fue realizado utilizando [Python](https://www.python.org/downloads/) versión 3.12.4.


## Tabla de contenido

- [Pre-requisitos](#pre-requisitos)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Ejecución](#ejecución)
    - [Variables de entorno](#variables-de-entorno)
    - [Ejecución Standalone](#ejecución-standalone)
        - [Instalación](#instalación)
        - [Ejecución](#ejecución-1)
    - [Ejecución con Docker](#ejecución-con-docker)
- [Pruebas unitarias](#pruebas-unitarias)
- [License](#license)


## Pre-requisitos

Para levantar este proyecto necesitarás:

* [Python](https://www.python.org/downloads/) (con virtualenv)
* Docker.
* Copia local de este repositorio.


## Estructura del proyecto


```
📦 Recipe Book API
│   📄 .env.template                                     # Template del archivo para las variables de entorno.
│   📄 .env.test                                         # Archivo con las variables de entorno para los tests unitarios.
│   📄 .gitignore                                        # Exclusión de archivos no deseados en el repositorio.
│   📄 docker-compose.yml                                # Orquestación de contenedores para desarrollo/despliegue.
│   📄 Dockerfile                                        # Archivo para despliegue con docker.
│   📄 populate_script.py                                # Script para poblar datos iniciales.
│   📄 README.md                                         # Usted está aquí.
│   📄 requirements.txt                                  # Definición de dependencias del microservicio.
├───📁 images                                            # Imagenes de los ingredientes de prueba para poblar.
│       🖼️ black-pepper.png
│       🖼️ butter.png
│       🖼️ carrot.png
│       ...
├───📁 src                                               # Código fuente del microservicio.
│   │   📄 main.py                                       # Punto de entrada de la aplicación.
│   ├───📁 db                                            # Clases para conexión a base de datos.
│   │       📄 database.py
│   │       📄 database_util.py
│   ├───📁 errors                                        # Clases interceptoras.
│   │       📄 errors.py
│   │       📄 exception_handlers.py
│   ├───📁 models                                        # Modelos para base de datos y enums.
│   │   │   📄 db_models.py
│   │   └───📁 enums
│   │           📄 measurement_unit.py
│   ├───📁 routers                                       # Definición de rutas y endpoints.
│   │   │   📄 health_check_router.py
│   │   │   📄 ingredient_router.py
│   │   └───📁 utils                                     # Dependencias e inyecciones comunes.
│   │           📄 dependencies.py
│   ├───📁 schemas                                       # Esquemas Pydantic para validación de datos.
│   │       📄 pydantic_schemas.py
│   └───📁 services                                      # Clases con lógica de negocio.
│           📄 ingredient_service.py
└───📁 tests                                             # Pruebas unitarias del sistema.
    │   📄 test_ingredient_router.py
    │   📄 test_health_check_router.py
    └───📁 config                                        # Configuración para pruebas.
            📄 conftest.py
            📄 postgres_test_container.py

```

Este es un microservicio que utiliza Python y FastAPI para ejecutar el servidor y pytest para ejecutar las pruebas unitarias. En general, hay dos carpetas principales: `src` y `tests`, así como algunos archivos de soporte.

- `.env.template`: Archivo de plantilla Env utilizado para definir variables de entorno. Consulte la sección  [Variables de entorno](#variables-de-entorno).
- `.env.test`: Archivo utilizado para definir variables de entorno para las pruebas unitarias. Consulta la sección [Variables de entorno](#variables-de-entorno).
- Dockerfile: Definición para construir la imagen Docker del microservicio. Consulta la sección [Ejecución Docker Compose](#ejecución-docker-compose).

## Ejecución

### Variables de entorno

El servidor FastApi y las pruebas unitarias utilizan variables de entorno para configurar las credenciales de la base de datos y encontrar algunas configuraciones adicionales en tiempo de ejecución. A alto nivel, esas variables son:


- DB_USER: Usuario de la base de datos
- DB_PASSWORD: Contraseña de la base de datos
- DB_HOST: Host de la base de datos
    Dependiendo de cómo se ejecute la aplicación se debe usar un valor u otro:
    -  Ejecución Standalone: `localhost`
    -  Ejecución Docker Compose: `app_db`
- DB_PORT: Puerto de la base de datos
- DB_NAME: Nombre de la base de datos
- VERSION: Versióon de la aplicación
- SECRET_TOKEN: Token secreto para las solicitudes hacia el microservicio
- APP_PORT: Puerto en el qué queremos desplegar la aplicación
- ENV: Ambiente a ejecutar (opcional, por defecto `development`)

  Valores:
    -  `development`
    -  `test` 

Estas variables de entorno deben especificarse en los archivos `.env` y `.env.test`. El segundo archivo ya está provisto, pero el primero debe crearse basado en la plantilla `.env.template` en la raíz de la carpeta del microservicio.

Como se mencionó anteriormente, tenemos dos archivos de entorno dentro de la carpeta del microservicio:
- `.env.template`
Este archivo contiene una plantilla de la estructura que el archivo `.env` utilizado por el servidor FlastApi requiere para funcionar así como la ejecución con Docker Compose.
- `.env.test`
Este es el archivo de entorno utilizado por pytest para ejecutar las pruebas unitarias.

### Ejecución Standalone

#### Instalación

* Abrir una terminal en la raíz del proyecto y ejecutar los siguientes comandos para instalar `Recipe Book API`:

    <details>
    <summary>Linux/MacOS</summary>
    <pre><code>python -m venv venv
  . venv/bin/activate
  pip install -r requirements.txt</code></pre>
    </details>

    <details>
    <summary>Windows</summary>
    <pre><code>python -m venv venv
  .\venv\Scripts\activate
  pip install -r requirements.txt</code></pre>
    </details>
    
#### Ejecución

1. Cree una base de datos temporal con docker usando el siguiente comando:
   ```
    docker run -d --name postgres_db -e POSTGRES_USER={DB_USER} -e POSTGRES_PASSWORD={DB_PASSWORD} -e POSTGRES_DB={DB_NAME} -p {DB_PORT}:{DB_PORT} postgres
    ```

    **Nota**: Estos valores deben ser iguales a los del archivo .env.  

2. En el archivo .env de la raíz del microservicio, cambie la variable DB_HOST por `localhost`.
3. Abrir una terminal en la raíz del proyecto y ejecutar los siguientes comandos para levantar `Recipe Book API`:

    <details>
    <summary>Linux/MacOS</summary>
    <pre><code>. venv/bin/activate
   uvicorn src.main:app --reload --port 3000</code></pre>
    </details>

    <details>
    <summary>Windows</summary>
    <pre><code>.\venv\Scripts\activate
   uvicorn src.main:app --reload --port 3000</code></pre>
    </details>

    **Nota**: Deberá tener en ejecución una base de datos PostgreSQL para poder utilizar el API.


### Ejecución con Docker

Para ejecutar el microservicio con Docker, se debe utilizar el archivo `docker-compose.yml` que se encuentra en la raíz del proyecto. Este archivo define los servicios necesarios para ejecutar el microservicio, incluyendo la base de datos PostgreSQL.
Para levantar el microservicio con Docker, siga estos pasos:
1. Asegúrese de tener Docker instalado y en ejecución en su máquina.
2. En el archivo .env de la raíz del microservicio, cambie la variable DB_HOST por `app_db`.
3. Abra una terminal en la raíz del proyecto y ejecute el siguiente comando:

    ```bash
    docker-compose up --build
    ```

Esto construirá la imagen del microservicio y levantará los servicios definidos en el archivo `docker-compose.yml`.
   

## Pruebas unitarias

* Abra una terminal en la raíz del proyecto y ejecute los siguientes comandos para correr las pruebas.

    <details>
    <summary>Linux/MacOS</summary>
    <pre><code>. venv/bin/activate
  pytest --cov-fail-under=70 --cov=src --cov-report=html</code></pre>
    </details>

    <details>
    <summary>Windows</summary>
    <pre><code>.\venv\Scripts\activate
  pytest --cov-fail-under=70 --cov=src --cov-report=html</code></pre>
    </details>

  **Nota**: Deberá tener en ejecución Docker, ya que lo usamos en las pruebas unitarias para TestContainers.


## License

Copyright © MISW4410 - Modernización de Software