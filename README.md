# Drunklandia API

This repository houses the REST API for <a href="https://github.com/jaredeiseman/drunklandia-app">Drunklandia</a>, an application for locating happy hours in your area.

To run this project, please have at least Python3.6, along with virtualenv installed on your computer.

After cloning the repo, and activating your virtual environment, run "pip install -r requirements.txt"

You will then need to run the following commands from your terminal in the root directory of the project:

python manage.py makemigrations<br/>
python manage.py migrate<br/>
python manage.py createsuperuser

Finally, you can run the server with "python manage.py runserver".

The browsable API can be accessed via localhost:8000, and the Django admin panel at localhost:8000/admin
