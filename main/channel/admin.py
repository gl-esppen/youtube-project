# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from channel.models import Theme, Thumb, Comment, Video


class ThemeAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_field=['name']

    fieldsets=(
        ('Theme Information', {
            'fields': ('name',), 
        }),
    )


class ThumbAdmin(admin.ModelAdmin):
    list_display=('video', 'time', 'is_positive',)
    list_filter=('is_positive',)
    search_field=['video__title']

    fieldsets=(
        ('Video Information', {
            'fields': ('video',), 
        }),
        ('Thumb Information', {
            'fields': ('time','is_positive'), 
        }),
    )


class CommentAdmin(admin.ModelAdmin):
    list_display=('video', 'time', 'is_positive',)
    list_filter=('is_positive',)
    search_field=['video__title']

    fieldsets=(
        ('Video Information', {
            'fields': ('video',), 
        }),
        ('Comment Information', {
            'fields': ('time','is_positive',), 
        }),
    )


class VideoAdmin(admin.ModelAdmin):
    list_display=('title', 'date_uploaded', 'views', 'get_themes',)
    list_filter=('title', 'themes__name',)
    search_field=['title', 'themes__name']

    fieldsets=(
        ('Video Information', {
            'fields': ('title','date_uploaded','views'), 
        }),
        ('Theme Information', {
            'fields': ('themes',), 
        }),
    )

    def get_themes(self, obj):
        return "\n".join([a.name for a in obj.themes.all()])



admin.site.register(Theme, ThemeAdmin)
admin.site.register(Thumb, ThumbAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Video, VideoAdmin)
