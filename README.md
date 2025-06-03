* read the comments in the visiting files.
visit:

1. foot/views.py
2. foot/urls.py

3. voyage/urls.py

4. to run the project create a virtual environment.
5. activate the virtual env.
6. cd voyage
7. finally run the project using "py manage.py runserver"

--------------------------------------------------------------------
* steps to create RESTAPI
* run the cmd "pip install djangorestframework"
* then add the "rest_framework" to voyage/setting.py.INSTALLED_APPS
* 
1. create a folder named api within foot app->(foot/api).
2. within api folder create these file (api/views.py, __init__.py, urls.py AND serialozers.py)

  * go to voyage/urls.py and mention api/urls path
    
3. Then go to the api/views.py and create one method (getRooms)
4. Go to api/urls.py and the following paths:
   -> path('', views.getRoutes),
    path('rooms/', views.getRooms)
5. Run the project and try fetching the urls api/urls created.
6. Then create second method into api/views.
7. Then go to serializers and create the class as provided.
8. Then add the 3rd and fianl url and run project, and try fetching the data with the specific id.
9. Done!!
