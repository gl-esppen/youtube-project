# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime


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

    def __unicode__(self):
        return self.video.title    


class Comment(models.Model):
    is_positive = models.BooleanField(verbose_name='Liked?')
    time = models.DateTimeField(verbose_name='Date/Time')
    video = models.ForeignKey('Video', verbose_name='Video')

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __unicode__(self):
        return self.video.title 


class Video(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    date_uploaded = models.DateTimeField(verbose_name='Date of Upload')
    views = models.IntegerField(default=0, verbose_name='Number of Views')
    themes = models.ManyToManyField(Theme, verbose_name='Themes')

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
    
    def __unicode__(self):
        return self.title

    #Counting de thumbs up
    def thumbs_up(self):
        return Thumb.objects.filter(
            is_positive=True).count()

    #Counting de thumbs down
    def thumbs_down(self):
        return Thumb.objects.filter(
            is_positive=False).count()

    #Counting de comments up
    def positive_comments(self):
        return Comment.objects.filter(
            is_positive=True).count()

    #Counting de comments down
    def negative_comments(self):
        return Comment.objects.filter(
            is_positive=False).count()

    #Counting days since upload
    def days_since_upload(self):
        return (datetime.date.today() - self.date_uploaded).days

    def timefactor(self):
        return max(0, 1 - self.days_since_upload()/365)

    def positivefactor(self):
        return (0.7 * self.good_comments()) + (0.3 * self.good_thumbs())

    def good_comments(self):
        return self.positive_comments() / (self.positive_comments() +  self.negative_comments())

    def good_thumbs(self):
        return self.thumbs_up()  / (self.thumbs_up() + self.thumbs_down())

    def score(self):
        return self.views * self.timefactor() * self.positive_comments()

    # Formula sucesso do canal
    # Filtro pelo sucesso do canal, que usa a formula
    # No save, nao permitir video com mais de 1 ano


