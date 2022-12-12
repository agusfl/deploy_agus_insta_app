# Demo de la app:

https://user-images.githubusercontent.com/64185026/206621802-6d21cd52-aa19-45ba-9ea6-0812d9f8f116.mp4

# Instrucciones para correr el programa y la aplicacion web:

>Seguir los siguientes pasos para poder ver quienes no te siguen y vos si en ``instagram``.

>**Importante:** Ver comenatarios y explicaciones del codigo dentro de los scripts.

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

>**Nota 1**: Ver en este [link](https://stackoverflow.com/questions/39406177/managing-contents-of-requirements-txt-for-a-python-virtual-environment) info sobre como hacer el archivo de ``requirements.txt`` (es con el comando: ```pip freeze > requirements.txt```)
El pip freeze lo que hace es listar todas las dependencias instaladas y con el simbolo de mayor (>) se le dice que mande el output al archivo ``requirements.txt`` (en caso que ya exista lo sobreescribe y sino lo crea).

>**Nota 2**: En este [link](https://stackoverflow.com/questions/51863155/do-we-need-to-upload-virtual-env-on-github-too) se explica porque no es bueno incluir la carpeta ``venv`` en github, en cambio lo correcto seria lo que comentaba mas arriba del archivo **"requirements.txt"**.

## Pasos para correr el programa de ``Agus insta app``:

### Primera version:

En una primera version que se puede ver en el repo [code_tests](https://github.com/agusfl/code_tests/tree/main/instagram/instaloader_module) en la carpeta de instagram
se corria en 3 pasos, corriendo primero el programa **"instaloader_module.py"** y luego moviendo el archivo generado **"not_following_you.txt"** hacia la carpeta de 
web_flask y por ultimo ejecutabamos el programa **"app.py"** para ver los resultados en la pagina web creada con flask en python.

### Segunda version:

En una segunda instancia decidi crear este repo (deploy_insta_app) donde hice varios cambios en la aplicacion de flask y cree varios endpoints y paginas web usando **html**, **css**, **javascript**, **jinja templates**, **boostrap** y mas..
De esta forma pude poner mis conocimientos a prueba y hacer un proyecto como fullstack developer encargandome tanto de la logica del back-end como del front.
Fue un lindo desafio y se aprendio mucho, **en los comentarios del codigo pongo referencias de donde saque la informacion y varias aclaraciones**.

Una de las grandes cosas que logre en esta segunda etapa fue conectar al front con el back y mandar datos desde el front para el back, por lo tanto para correr el programa solo basta con ejecutar **app.py** con el siguiente comando:

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

## Vercel - deploy:

Una vez terminado el proyecto voy a intentar hacer el deploy con ``vercel`` --> info sobre **vercel** en este [link](https://vercel.com/docs).

Ya hice algunas pruebas para hacer el deploy con este proyecto con vercel y cuando haces el deploy automaticamente un **bot** de vercel te manda mails cada vez que haces un commit en el repo. Para desactivar esta opcion cree el archivo ``vercel.json`` donde podes configurar determinadas cosas, entre esas esta la opcion: 

"github": {
      "silent": true
     }

Use dicha opcion para que no me lleguen notificaciones cada vez que hago un nuevo commit en el repo.

Info sobre la configuracion de vercel en este [link](https://vercel.com/docs/concepts/git/vercel-for-github?utm_source=github&utm_medium=marketplace&utm_campaign=vercel-app).

## Notas: 

* **IMPORTANTE** tener en cuenta que cuando se dan errores y no se genera el ``archivo txt`` con la lista de personas que seguis y no te siguen suele ser por problemas de que bloquearon la cuenta de ig con la que nos loggeamos por lo tanto en estos casos conviene entrar manualmente a instagram y fijarse si la cuenta esta bloqueada y en caso de que lo este desbloquearla.
* Esta es la [pagina](https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application) de donde saque la info para **"linkear" y poder mandar cosas desde el front al back**, en mi caso mando el nombre del ``usuario de ig`` que se quiere buscar atraves de un formulario en el front al back end.
* Se usa un archivo ``.env`` para setear las variables de entorno, como ser: el usuario y contraseña del usuario con el que nos loggeamos en instagram.
- Info sobre .env file y como usarlo en este [link](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1).
* Si solo queremos ver la lista de personas que no te siguen impresa en la consola correr solo el siguiente programa: [read_instaloader_file.py](https://github.com/agusfl/code_tests/blob/main/instagram/instaloader_module/web_flask-instaloader_page/read_instaloader_file.py) luego de haber realizado el ``paso 1 y 2`` explicados en este [link](https://github.com/agusfl/code_tests/blob/main/instagram/instaloader_module/README.md).
* Info para hacer el **spinner** mientras se cargan los datos: use el ``chatbot de GPT (IA)`` y tmb la info de ``bootstrap`` de este [link](https://getbootstrap.com/docs/5.2/components/spinners/), hice comentarios en el codigo de: search_user.html


## Authors :pen:

 * [Agustin Flom](https://www.linkedin.com/in/agustin-f/)
 
## Licence :lock:

This project is published only for educational purposes. It must not be distributed without permission of the authors.
