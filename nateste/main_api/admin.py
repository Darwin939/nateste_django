from django.contrib import admin
from .models import Review, Profile,Order

admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Review)
