Commands:

1. Create project: `django-admin startproject my_nws`
2. Create app: `python .\manage.py startapp current`
3. Create urls.py in the app and reference in my_nws/urls.py
4. Add app to settings.py in `INSTALLED_APPS`
5. Implement views.py using templates in templates\current
6. Create database (if needed)
    * Implement database tables in models.py for the app
    * Create migration`python .\manage.py makemigrations current`
    * To the see the SQL: `python .\manage.py sqlmigrate current 0001`
    * Apply migration: `python .\manage.py migrate`
    * To interact directly with the database: `python .\manage.py shell`
    * Add app model to admin rights by changing admin.py
7. Create an admin user: `python .\manage.py createsuperuser`    
8. Run Server: `python .\manage.py runserver`

