from django.contrib import admin
from . import models

# Register your models here.
class CardsAdmin(admin.ModelAdmin):
    list_display=('id','title',)

admin.site.register(models.Card,CardsAdmin)