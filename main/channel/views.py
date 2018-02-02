# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from . import models

# Create your views here.
def main(request):
	context = {
		'popular_themes': models.Theme.get_popular_themes(),
	}
	return render(request, 'main.html', context)