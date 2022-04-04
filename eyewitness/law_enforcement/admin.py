from django.contrib import admin
from .models import User, Customer, Employee, Photo, Case

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Photo)
admin.site.register(Case)