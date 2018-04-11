from django.contrib import admin
from music.models import Album, Song


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'id')


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'album')
    list_filter = ('album', 'duration')

# class EventAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
