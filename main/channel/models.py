# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Theme(models.Model):
	name = models.CharField(max_length=150, verbose_name='Name')

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"
    
    def __unicode__(self):
        return self.name


class Thumb(models.Model):
	is_positive = models.BooleanField(verbose_name='Liked?')
	time = models.DateTimeField(verbose_name='Date/Time')
	video = models.ForeignKey('Video', verbose_name='Video')

    class Meta:
        verbose_name = "Thumb"
        verbose_name_plural = "Thumbs"
    


class Comment(models.Model):
	is_positive = models.BooleanField(verbose_name='Liked?')
	time = models.DateTimeField(verbose_name='Date/Time')
	video = models.ForeignKey('Video', verbose_name='Video')

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Video(models.Model):
	title = models.CharField(max_length=150, verbose_name='Title')
	date_uploaded = models.DateTimeField(verbose_name='Date of Upload')
	views = models.IntegerField(default=0, verbose_name='Number of Views')
	themes = models.ManytoManyField(Theme, verbose_name='Themes')

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
    
    def __unicode__(self):
        return self.title