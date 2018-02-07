from django import template
from django.template import Library

register=template.Library()

@register.filter
def return_item(l,i):
  print i
  try:
  	print l[i]
  	return l[i]
  except:
    return None