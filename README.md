# Querios
Question/answer Single Page Application using Django, Django REST Framework and Vue.js


## Installation/How to use
1. Currently the code is set with DEBUG=True in settings.py with Django routing to index.html template, change DEBUG=False to route it to index-dev.html or go to core/views.py and changing "if not settings.DEBUG" to "if settings.DEBUG"


2A. (DEVELOPMENT MODE) If using the index-dev.html template you need to navigate to the frontend folder with terminal/command-prompt and run the command "npm run serve" and run the Django development server by going to the Querios folder with manage.py and use the command "python manage.py runserver". Then use your preferred browser (Chrome, Safari, Firefox, etc.) with address "127.0.0.1:8000"


2B. (PRODUCTION MODE - Default) If using the code as is without changing DEBUG=True or changing the if statement in core/views.py run the Django development server from your terminal/command prompt by going to the Querios folder with manage.py "python manage.py runserver" and going to your preferred browser with address "127.0.0.1:8000"


## users
Data (serializers, views) regarding users API endpoint

## questions
Questions/answers endpoints with the API logic

## frontend
Frontend single page application rendered using Vue.js (and webpack loader for debugging).
