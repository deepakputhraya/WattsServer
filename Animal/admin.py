from django.contrib import admin
from Animal.models import Animal,Adopt,Story

class AnimalAdmin(admin.ModelAdmin):
  list_display = ('name', 'breed')


class StoryAdmin(admin.ModelAdmin):
  list_display = ('animal', 'description')


class AdoptAdmin(admin.ModelAdmin):
  list_display = ('animal', 'description')


admin.site.register(Animal,AnimalAdmin)
admin.site.register(Adopt,AdoptAdmin)
admin.site.register(Story,StoryAdmin)