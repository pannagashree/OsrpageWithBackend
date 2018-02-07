# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import psycopg2
from django.shortcuts import render
from webpage_display.models import ROTI,NAAN,KULCHA,PARATHA
from django.http import JsonResponse
indian_breads=[[0,'ROTI'],[1,'NAAN'],[2,'KULCHA'],[3,'PARATHA']]
mod=[ROTI,NAAN,KULCHA,PARATHA]
def menu(request):
	Ib_list=[]
	for y in mod:
		rows=y.objects.all()
		item_list=[]
		for row in rows:
			x=[]
			x.extend((row.id,row.item_name,row.cost))
			item_list.append(x)
		Ib_list.append(item_list)
	if(request.method=='GET'):
		return render(request,'menu.html',{'variety':indian_breads,'lists':Ib_list	})
def review(request):
	if(request.method=='GET'):
		return render(request,'review.html')
def order_info(request):
	data={}
	inum=request.GET.get('item_no',None)
	myconnection=psycopg2.connect(host="localhost",user="pannaga",password='pannaga1@~',dbname="osr")
	cur=myconnection.cursor()
	cur.execute("select * from webpage_display_menu where id=%s",(inum,))
	for i_no,name,cost in cur.fetchall():
   		data.update({"iname":name})
   	return JsonResponse(data)