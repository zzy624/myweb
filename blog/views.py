#-*-coding:utf-8-*-
from blog.models import Blog
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    blog_list = Blog.objects.all()
    # username = request.COOKIES.get('username','') #读取浏览器cookie
    username = request.session.get('username','') #读取浏览器session
    user = username[0]
    return render_to_response('index.html',
                              {'user':user,'blogs':blog_list})

def login(request):
    return render(request,'login.html')

def login_action(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    users_ = [username]
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user) #验证登录
        response = HttpResponseRedirect('/index/')
        # response.set_cookie('username',username,3600) #用户名cookie
        request.session['username'] = users_ #将session信息写到服务器
        return response
        # return HttpResponse('login success')
    else:
        return render_to_response('login.html',
                                  {'error':'username or password error!'},
                                  context_instance=RequestContext(request))
@login_required
def logout(request):
    response = HttpResponseRedirect('/login/') #返回登录页面
    # response.delete_cookie('username') #清理cookie里保存username
    del request.session['username'] #清理用户session
    return response