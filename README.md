# Flask Project Builder


## GET YOUR FLASK BOILERPLATE
Fill out the form and get your code!

- **Project Name**   
Do not use spaces in your project name. Prefer underscores instead spaces.

- **Application Factory Pattern**   
Indicates that you want to create a new Flask project on [Application Factory Pattern](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/). The application factory is an architectural model for applications


- **SQLAlchemy**   
Indicates that you want to install [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) in your project.

- **Dynaconf**   
Indicates that you want to install [Dynaconf](https://dynaconf.readthedocs.io/en/docs_223/) in your project.

- **.tar.gz / .zip**   
Choose the file format to download

## AFTER GETTING YOUR FILE

1. Unzip the file you downloaded:  
   ~~~sh
   $ tar -vzxf project_name.tar.gz  # if you chose .tar.gz
   $ unzip project_name.zip         # if you chose .zip
   ~~~
2. Enter the project_name directory:
   ~~~sh
   $ cd project_name
   ~~~
3. Create and update your virtual environment:
   ~~~sh
   $ python3 -m venv .venv
   $ source .venv/bin/activate
   $ pip install --upgrade pip
   ~~~
4. Run make install (or make install-dev):
   ~~~sh
   $ make install
   ~~~
   _ps. `make install-dev` will install some development tools for you_

## IMPORTANT

If you chose the Application Factory Pattern, don't forget to update the FLASK_APP environment variable:
~~~sh
$ export FLASK_APP=project_name/app.py
~~~

If you want to run flask in development mode, update the FLASK_ENV environment variable:
~~~sh
$ export FLASK_ENV=development
~~~

If you are using the Application Factory Pattern and want to use the `flask-toolbar`, run the command:
> ~~~sh
> $ pip install flask-toolbar
> ~~~
> 
> and uncomment the following line in app.py
> ~~~toml
> # toolbar.init_app(app)
> ~~~
> if you are using Dynaconf, uncomment the following line:
> ~~~toml
> # "project_name.ext.toolbar:init_app" 
> ~~~

In the Makefile file, we have some useful commands, which we use with the make command, such as:

| Command            | What he does                                         |
| ------------------ | ---------------------------------------------------- |
| `make clean`       | clears the project folder                            |
| `make install`     | install our project as a package python              |
| `make install-dev` | similar to install, but with requirements-dev.txt    |
| `make test`        | run tests                                            |
| `make init-db`     | starts and updates the db (if you choose SQLAlchemy) |
| `make format`      | formats the files (needs: isort and black)           |

<br>

### _This python project was created by **Cesar Godoi** and **Jady Godoi** during [Curso de Desenvolvimento Web](http://skip.gg/curso-flask-codeshow) taught by **Bruno Rocha**._
_August 2020_ 