from .base import *

# https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ROOT_URLCONF = 'project_blog.urls_production'
