from blog.models import Blog
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    blog_list = Blog.objects.all()
    return render_to_response('index.html',{'blogs':blog_list})