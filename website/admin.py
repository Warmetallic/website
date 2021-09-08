from django.contrib import admin

from .models import Image
# Register your models here.

class ImageAdmin(admin.StackedInline):
	model=Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	pass