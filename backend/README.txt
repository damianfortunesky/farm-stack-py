Lo primero a realizar es crear un proyecto de backend, para esto:

    1. Crear entorno virtual en python, si ya esta python instalado:

            . Terminal -> python -m venv [nombreCarpeta]

            . Esto sirve para aislar el proyecto e indicar que las dependencias instaladas son unicamente para el proyecto en cuestion.

            . F1 + ">Python: Select Interpreter" + lista opciones para ejecutar python + selecionar entorno virtual creado [venv]

    2. Config proyecto:

            . pip install fastapi uvicorn motor

            . Instalar DB, en este caso mongoDB

            . Instalar Extension visual Thunder Client para testear los endpoints

    3. Desarrollo:

            . Crear mi servidor y definir las rutas en main.py

            . Conectar app a mongoDB en database.py y crear operaciones CRUD

            . Conectar mis funciones del modelo (querys) de database.py con mis rutas de main.py (controlers). 
            
                Simplemente ejecutar las f(x) del modelo en las funciones de las rutas. 

             

            

    

