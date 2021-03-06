from django.contrib import admin
from .models import Register
from .models import PressRelease
from .models import Photo
from .models import Event 

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'album')


admin.site.register(Photo, PhotoAdmin)

admin.site.register(Register)

admin.site.register(PressRelease)

admin.site.register(Event)
