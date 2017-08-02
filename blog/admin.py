from django.contrib import admin
# import Post modell a models.py bol
from .models import Post

#látszódjon a modell ezért regisztrálnunk kell
admin.site.register(Post)

# Register your models here.
