#_*_ coding: utf-8 _*_
from django.http import HttpResponse
from django.shortcuts import render

def hh(request):
	return HttpResponse("RNG66")
	
def hello(request):
	context = {}
	context['hello'] = 'RNG666!'
	return render(request,'hello.html',context)