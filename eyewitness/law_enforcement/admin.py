from django.contrib import admin
from .models import User, Witness, Officer, Photo, Case, LineUp

admin.site.register(User)
admin.site.register(Witness)
admin.site.register(Officer)
admin.site.register(Photo)
admin.site.register(Case)
admin.site.register(LineUp)