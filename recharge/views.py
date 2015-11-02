from django.shortcuts import render, redirect, render_to_response
# Create your views here.
#view for homepage
def home(request):
	render(request,'recharge/base.html')
