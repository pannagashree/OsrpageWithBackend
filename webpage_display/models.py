# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Menu(models.Model):
	item_name=models.TextField(max_length=50)
	cost=models.IntegerField()
class ROTI(Menu):
	pass
class NAAN(Menu):
 	pass
class KULCHA(Menu):
	pass
class PARATHA(Menu):
	pass 