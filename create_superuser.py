# create_superuser.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from accounts.models import CustomUser  # Import your custom user model

username = 'tomiwa'
email = 'tomadeaga@gmail.com'
password = 'smartkid'

if not CustomUser.objects.filter(username=username).exists():
    CustomUser.objects.create_superuser(username=username, email=email, password=password)
    print('Successfully created new superuser')
else:
    print('Superuser already exists')
