from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
#from django.template.loader import get_template
#from django.template import Context
from models import news
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from models import ipl_scores 
from forms import newsform

def login(request):
	c={ }
	c.update(csrf(request))
	return render(request,'login.html')

def auth_view(request,id=1):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		a=str(User.objects.get(username=user.username).id)
		
		return HttpResponseRedirect('/accounts/loggedin/'+(a))
		'''
		id=User.objects.get(id=1)
		args = {}
	 	args.update(csrf(request))
	 	return render(request,"loggedin.html", args)
'''
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
	return render(request,'invalid_login.html')

def logout(request):
	auth.logout(request)
	return render(request,'logout.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
     	else:
     		return HttpResponseRedirect('/accounts/bad_request')
        
    else:
    	
        form = UserCreationForm()
    	args = {}
    	args.update(csrf(request))

    
    	args['form'] = UserCreationForm()
    	args['login'] = True

    	return render(request,'register.html', args)


def register_success(request):
    return render(request,'register_success.html')


def home(request):
	args = {}
	args.update(csrf(request))

	args['news'] = news.objects.all().order_by('-pub_date')
	return render(request,"home.html", args)

def bad_request(request):
	return render(request, "bad_request.html")

def add_news(request):
	if request.POST:
		form = newsform(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')

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
