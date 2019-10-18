from django.contrib import admin

# Import Post class from models.py
from .models import Post


# Register our Post class with the admin site
admin.site.register(Post)
