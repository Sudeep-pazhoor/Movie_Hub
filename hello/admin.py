from django.contrib import admin
from hello.models import Movie

admin.site.register(Movie)

# Delete or comment out LogMessage admin registration if present
# from .models import LogMessage
# admin.site.register(LogMessage)

