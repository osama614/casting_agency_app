# casting_agency_app

## Introduction
Casting Agency is an web App that can show movies and actors.  
the App has three platforms for three roles which are  
visit : https://casting-agency-osama.herokuapp.com/

- **Casting Assistant**    
who can :  
   - See all the Movies and Actors

- **Casting Director**   
who can :  
   - See all the Movies and Actors
   - Edit Actors
   - Updata Actors and Movies
   - Delete Actors
  
- **Excutive Producer**  
who can :  
   - See all the Movies and Actors
   - Edit Actors and Movies
   - Updata Actors and Movies
   - Delete Actors and Movies
 
 ### Tech Stack

Our tech stack will include:

* **SQLAlchemy ORM** to be our ORM library of choice
* **PostgreSQL** as our database of choice
* **Python3** and **Flask** as our server language and server framework
* **Flask-Migrate** for creating and running schema migrations
* **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) for our website's 
frontend
* **Auth0** as our Authanticaton and Authorization third party provider

### Main Files: Project Structure

  ```sh
  ├── README.md
  ├── app.py *** the main driver of the app. Includes your SQLAlchemy models.
                    "python app.py" to run after installing dependences
  ├── flask_env.env *** Database URLs, CSRF generation, etc
  ├── forms.py *** Your forms
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ├── static
  │   ├── css 
  │   ├── font
  │   ├── img
  │   └── js
  ├── templates
  ├── Procfile *** for heroku deployment
  ├── wsgi.py *** for gunicorn start 
  ├── auth.py *** for handling Authanticaton and Authorization of the app
  ├── migrations 
  ├── manage.py *** for handling migrations versions
  ├── models.py
  ├──test_flaskr *** updated to handling your endpoints
  ```
##Overall:
* Models are located in the `models.py`.
* Controllers are also located in `app.py`.
* The web frontend is located in `templates/`, which builds static assets deployed to the web server at `static/`.
* Web forms for creating data are located in `form.py`

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/casting_agency_app` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 



## Running the server

From within the `/casting_agency_app` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```
then run your all environment variables
ex: 
```bash
export AUTH0_DOMAIN=YOUR_AUTH0_DOMAIN
```
then run the APP by
```bash
flask run
```
Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Database Migrations
With Postgres running, setup a database schema using the Flask-migrations file provided. From the `/casting_agency_app` folder in terminal run:
```bash
flask db upgrade
or
python manage.py db upgrade
```
## URL
this the url for the App on heroku.  
> (https://casting-agency-osama.herokuapp.com/)
## Deployment Instructions  
From within the `/casting_agency_app` directory in trminal run :  
```bash
git init
```
then login to your heroku account from terminal by run :  
```bash
heroku login
```
now you can create your app on heroku by run : 
```bash
heroku create name_of_your_app
```
The output will include a **git url** for your Heroku application. Copy this as, we'll use it in a moment.  
Now if you check your Heroku Dashboard in the browser, you'll see an application by that name.  
But it doesn't have our code or anything yet - it's completely empty. Let's get our code up there.  

### Add git remote for Heroku to local repository
Using the git url obtained from the last step, in terminal run:  
```bash
git remote add heroku your_heroku_git_url
```
### Add postgresql add on for our database
Heroku has an addon for apps for a postgresql database instance.  
Run this code in order to create your database and connect it to your application :  
```bash
heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application
```
**Now !** go to your heroku app dashboard then :  
1. hit *settings* button in nav bar  
2. hit *Reveal config vars* button and start to inter your Environment Variables.

## Push your APP
for Pushing your APP run that in the terminal :  
```bash
git push heroku master
```
## Setup your DB schema
run your migrations versions to setup your DB schema on heroku postgres DB by :
```bash
heroku run python manage.py db upgrade --app name_of_your_application
```
### Now you can check your app and see it works.
