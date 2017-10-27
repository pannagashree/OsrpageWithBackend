# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def menu(request):
	if(request.method=='GET'):
		return render(request,'indian_breads.html')