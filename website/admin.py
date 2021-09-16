from django.contrib import admin

from .models import Image, Games
# Register your models here.

class ImageAdmin(admin.StackedInline):
	model=Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	pass

class GameAdmin(admin.StackedInline):
	model=Games

@admin.register(Games)
class GameAdmin(admin.ModelAdmin):
	pass