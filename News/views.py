import urllib2
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import news
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from forms import newsform
from bs4 import BeautifulSoup



def login(request):
	args={}
	args.update(csrf(request))
	args['login']=True
	return render(request,'login.html',args)

def auth_view(request,id=1):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		a=str(User.objects.get(username=user.username).id)
		
		return HttpResponseRedirect('/accounts/loggedin/'+(a))
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request,id=1):
	args = {}
 	args.update(csrf(request))

 	args['loggedin'] = True
 	args['get_id']=User.objects.get(id=id)
 	args['news'] = news.objects.all().order_by('-pub_date')

	return render(request,'loggedin_home.html',args)

def invalid_login(request):
	args = {}
	args.update(csrf(request))
	args['invalid']=True
	return render(request,'invalid_login.html',args)

def logout(request):
	args = {}
 	args.update(csrf(request))
 	args['logout']=True
	auth.logout(request)
	return render(request,'logout.html',args)

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
     	else:
     		return HttpResponseRedirect('/accounts/bad_request', )
        
    else:
        form = UserCreationForm()
    	args = {}
    	args.update(csrf(request))

    	args['form'] = UserCreationForm()
    	args['register'] = True

    	return render(request,'register.html', args)


def register_success(request):
	args={}
	args.update(csrf(request))
	args['home']=True
	return render(request,'register_success.html',args)
    

def home(request):
	args = {}
	args.update(csrf(request))
	args['home']=True
	args['news'] = news.objects.all().order_by('-pub_date')
	return render(request,"home.html", args)


def bad_request(request):
	args = {}
	args.update(csrf(request))
	args['home']=True
	return render(request,"bad_request.html",args)


def add_news(request,id=1):

	a=str(request.build_absolute_uri())
	user_id = a.split('/')[-2]

	if request.POST:
		form = newsform(request.POST)
		if form.is_valid():
			form.save()
			link = str(form.cleaned_data['heading'])
			x = news.objects.get(heading=link)

			string_link=repr(link)
			url = urllib2.urlopen(link)
			soup = BeautifulSoup(url)
			title=soup.find('title').text
			x.title=title
			
			x.user_id=user_id

			form.save()
			x.save()
			args = {}
			args.update(csrf(request))
			args['add_news']=True
			args['title']=title
			args['get_id']=user_id

			return HttpResponseRedirect('/accounts/loggedin/'+(user_id))

	else:
		form = newsform()
		args = {}
		args.update(csrf(request))
		
		args['login'] = True
		args['form'] = form
		return render(request,'add_news.html', args)


def news_single(request,id=1):
	args = {}
	args.update(csrf(request))
	args['login']=True

	args['news']= news.objects.get(id=id)
	return render(request,"news_single.html", args)


def upvotes(request,id=1):
	args = {}
	args.update(csrf(request))

	obj= news.objects.get(id=id)
	upvotes=obj.upvote
	upvotes+=1
	obj.upvote = upvotes
	obj.save()

	return HttpResponseRedirect('/news/get/%s/' %id)

def content_added(request,id=1):
	a=str(request.build_absolute_uri())
	id = a.split('/')[-2]

	args = {}
	args.update(csrf(request))
	args['added']=True
	args['news']= news.objects.filter(user_id=id)
	return render(request,"content_added.html", args)