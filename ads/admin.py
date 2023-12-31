from django.contrib import admin
from .models import Ad, Fav

# Register your models here.

# hides the 'excluded' fields from the admin interface.
class AdAdmin(admin.ModelAdmin):
	exclude = ('picture', 'content_type')

admin.site.register(Ad, AdAdmin)
admin.site.register(Fav)
