from django.shortcuts import render,get_object_or_404
from .models import Blog
def home(request):
	bl=Blog.objects
	return render(request,'blog/home.html',{'blogs':bl})

def detail(request,blog_id):
	blogdetail=get_object_or_404(Blog,pk=blog_id)
	return render(request,'blog/detail.html',{'blog':blogdetail})