learning_blog is a web app that allows users to report the learning experience 
on topics they are interested in. The learning blog home page allows the user 
either to log in or register. Only logged users will be allow to create, add or 
posts and edit existing entries. 

The Web App was developed with Python ,Django, Bootstrap 3 , HTML.

The project is prepared to be deployed to Herokku with all the necessary changes
included. 

After deploying to Heroku you will have to set Environment variables :

SECRET_KEY=YOUR_DJANGO_SECRET_KEY
DEBUG_VALUE='False'
PRODUCTION_VALUE='True'

You will also need to adjust the variable ALLOWED_HOSTS in settings.py 
to include your website name
ALLOWED_HOSTS = ['YOUR_NAME_COMES_HERE.herokuapp.com'] 

During your setup you will be required by Heroku / Django to create a superuser.