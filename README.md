# Demo de la app:

https://user-images.githubusercontent.com/64185026/206621802-6d21cd52-aa19-45ba-9ea6-0812d9f8f116.mp4

# Instrucciones para correr el programa y la aplicacion web:

>Seguir los siguientes pasos para poder ver quienes no te siguen y vos si en ``instagram``.

## Requirementes a instalar:

Se recomienda primero que nada crear un entorno virtual de python con ``venv``, se puede crear en un entorno de windows de la siguiente manera:

```
python.exe -m venv venv
```

Una vez que se crea el entorno virtual con el comando anterior hay que **activarlo** con el siguiente comando:

```
.\venv\Scripts\activate
```

Antes de empezar con los pasos que detallo a continuacion hay que instalar las siguientes dependencias (librerias):

Con el siguiente comando se instalan todas las dependencias que se necesitan para que pueda correr la app y que estan definidas en ``requirements.txt``
```
pip install -r requirements.txt
```

>**Nota**: Ver en este [link](https://stackoverflow.com/questions/39406177/managing-contents-of-requirements-txt-for-a-python-virtual-environment) info sobre como hacer el archivo de ``requirements.txt`` (es con el comando: ```pip freeze > requirements.txt```)
El pip freeze lo que hace es listar todas las dependencias instaladas y con el simbolo de mayor (>) se le dice que mande el output al archivo ``requirements.txt`` (en caso que ya exista lo sobreescribe y sino lo crea).

## Pasos para correr el programa de ``Agus insta app``:

Para correr el programa solo basta con ejecutar **app.py** con el siguiente comando:

Desde un entorno de ``windows``:

```
python.exe .\app.py
```

Si se esta en un entorno de ``linux`` y se le dio permsios de ejecucion con: ``chmod u+x app.py`` y se puso el shebang correspondiente como ser: ``#!/usr/bin/python3``:

```
./app.py
```

Otra opcion es correrlo con el comando del framework ``flask``:

```
flask run
```
Como llamamos a nuestro archivo "app.py" al poner "flask run" se va a buscar por default el archivo llamado **app.py**.

**Importante:** Recordar crear un archivo ``.env`` con el usuario y clave de la cuenta de ig usada. 

## Notas: 

* **IMPORTANTE** tener en cuenta que cuando se dan errores y no se genera el ``archivo txt`` con la lista de personas que seguis y no te siguen suele ser por problemas de que bloquearon la cuenta de ig con la que nos loggeamos por lo tanto en estos casos conviene entrar manualmente a instagram y fijarse si la cuenta esta bloqueada y en caso de que lo este desbloquearla.

## Authors :pen:

 * [Agustin Flom](https://www.linkedin.com/in/agustin-f/)
 
## Licence :lock:

This project is published only for educational purposes. It must not be distributed without permission of the authors.
