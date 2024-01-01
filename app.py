#!/usr/bin/python3
"""
Script that starts a Flask web application
- Your web application must be listening on 0.0.0.0, port 5000
Flask es un framework minimalista escrito en Python que permite crear aplicaciones web rápidamente y con un mínimo número de líneas de código.
Está basado en la especificación WSGI de Werkzeug y el motor de templates Jinja2 y tiene una licencia BSD.
Por mas informacion ver las notas del tercer trimestre de Holberton en la parte del proyecto AirBnB_V2.
Use como referencia el codigo del github que tengo en el proyecto: holbertonschool-AirBnB_clone_v2 --> 7-states_list.py
- Ejemplo de una app de flask usando visual studio: https://code.visualstudio.com/docs/python/tutorial-flask#:~:text=To%20run%20the%20app%20outside,using%20python%20%2Dm%20flask%20run%20.
- Como conectar front con back usando flask: https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
"""
from flask import Flask, render_template, request, flash, url_for, redirect

# Se crea una instancia de flask con el nombre del archivo nuestro
app = Flask(__name__)
# Genere el string con el siguiente codigo: os.urandom(24).hex()
# Info sobre porque se usa una "SECRET_KEY": https://www.reddit.com/r/flask/comments/m0z7s1/need_some_help_understanding_the_use_of_a_flask/
app.config['SECRET_KEY'] = '6df63440284a1d432eb39ed1fed35a3b64d1bce64bf4bb9b'

@app.route("/", strict_slashes=False)
def index():
    """
    Ruta index de donde se redirigue a las demas rutas y es el home de la pagina.
    - strict_slasges = False -> Esta opción se usa para que si le pones un / (slash)
    al final de la ruta que tmb te lo tome y no te salga un error como que no se encontro la pagina.
    """

    return render_template("index.html")

@app.route('/search/', strict_slashes=False, methods=('GET', 'POST'))
def search_user():
    """
    Ruta para ir a seleccionar el usuario de instagram que queres que se busque en la app.
    - Buena info que segui como tutorial y explica como mandar info desde el front con formularios
    al back usando flask y "request": 
    https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
    """

    if request.method == 'POST':

        # Se obtiene el user_name escrito desde el front
        user_name = request.form['user_name']

        # Si no se puso ningun usuario y se hace submit se pone un cartel pidiendo que se indique un usuario
        if not user_name:
            flash('An instagram user name is required!')
        else:
            try:
                # Debugging - imprimo en pantalla de la consola lo que se mande en el submit del ig_user
                print(user_name)
                
                import instaloader
                # Import os and dotenv to allow the use of environmental variables from the .env file
                import os
                from dotenv import load_dotenv

                load_dotenv()

                # Loading instaloader object
                L = instaloader.Instaloader()

                # Username and password
                username = os.getenv('IG_USERNAME')
                password = os.getenv('IG_PASSWORD')

                # Login with username and password
                L.login(username, password)
                print(f"Successful login into: {username}")

                # instaloader profile object - aca es donde se pone el usuario (ig_user) del cual se quiere buscar que usuarios el sigue y no lo siguen
                # Recordar que para poder obtener los datos de dicho usuario se lo tiene que seguir con el usuario que se logea en este programita
                profile = instaloader.Profile.from_username(L.context, username)

                # Make a list of current followees
                logged_user_current_followees = [i.username for i in profile.get_followees()]

                # Si no se sigue al usuario con nuestro usuario de ig trucho se imprime en consola y en la pagina
                if user_name not in logged_user_current_followees:
                    print(f"User is not followed by {username}")
                    flash("Agus insta app does not follow this user please contact the team or select another user")
                else:
                    # Usuario del cual se quiere obtener los datos de seguidores
                    ig_search_user = user_name

                    # instaloader profile object - aca es donde se pone el usuario (ig_user) del cual se quiere buscar que usuarios el sigue y no lo siguen
                    # Recordar que para poder obtener los datos de dicho usuario se lo tiene que seguir con el usuario que se logea en este programita
                    profile = instaloader.Profile.from_username(L.context, ig_search_user)

                    # Make a list of current followers
                    current_followers = [i.username for i in profile.get_followers()]

                    # Make a list of current followees
                    current_followees = [i.username for i in profile.get_followees()]
                    
                    # Code to see who is not following you back:
                    # Defino una variable global para poder usarla aca y tmb en la ruta "app"
                    global not_following_you
                    not_following_you = []

                    for element in current_followees:
                        if element not in current_followers:
                            not_following_you.append(element)

                    # Se guardan las personas que no te siguen en un archivo llamado "not_following_you.txt" para poder trabajar con el archivo en otro programa
                    # y no tener que correr este programa muchas veces ya que la cuenta de ig con la que nos logeamos puede ser bloqueada.
                    with open('not_following_you.txt', 'w+') as f:
                        for person in not_following_you:
                            file = f.write(person+"\n")
                        print("The list of people who do not follow you has been successfully saved in the file: 'not_following_you.txt'")
                    
                    # Si se pasa un usuario se redirige a la pagina "app.html" en url_for hay que poner el nombre de la funcion por eso pongo go_to_app y no "app"
                    # en la funcion de go_to_app se va a renderizar la lista pasandole 'not_following_you' del usuario indicado.
                    return redirect(url_for('go_to_app'))
            except Exception:
                return render_template('internal_errors.html')

    return render_template('search_user.html')

@app.route('/app/', strict_slashes=False)
def go_to_app():
    """
    Ruta para ir a la app donde esta la lista de gente que seguis y no te sigue.
    """
    # Se trae la lista de personas que no te siguen y vos si usando la funcion creada en "read_instaloader_file.py" 
    # Se pasa la lista como variable para poder ser usada con jinja en el archivo "not_following_you.html"
    people_not_following_you = not_following_you

    return render_template('app.html', not_following_you=people_not_following_you)

@app.route('/last-searched-user/', strict_slashes=False)
def last_searched_user():
    """
    Ruta para ir a la lista  de gente que seguis y no te sigue del ultimo usuario buscado.
    De esta forma no hay que correr siempre la app (que demora unos segundos (20-30)) para
    poder ver los datos.
    - Para que funcione esta ruta se tiene que tener creado un archivo de "not_following_you.txt"
    Sino no va a tener de donde leer los nombres.
    """
    # Se pone el codigo en un try y un except para el caso de que no haya un archivo creado de "not_following_you.txt"
    try:
        # Name of the file that you want to read
        filename = "not_following_you.txt"

        # Open file and read the data
        with open(filename, 'r', encoding="utf-8") as f:
            read_data = f.readlines()

        # Se crea una nueva lista sacandole los saltos de linea a cada dato de "read_data" ya que se le habia puestos los saltos de linea para el txt.
        not_following_you = [item.strip() for item in read_data]

        # Se renderiza el template "app.html" pasandole como variable la lista de personas que no siguen al usuario y el usuario las sigue.
        return render_template('app.html', not_following_you=not_following_you)
    
    except Exception:
        return render_template("no_search_user.html")


if __name__ == "__main__":
    """
    Set host IP addres, port and debug mode:
    - El host se setea en: 0.0.0.0 para que sea accesible desde cualquier IP.
    - Se setea debug=True porque esto nos permite poder cargar interactivamente los cambios (auto reloade) y verlos en el navegador,
    sin tener que frenar y volver a correr el programa.
    """
    app.run(host='0.0.0.0', port=5000)
