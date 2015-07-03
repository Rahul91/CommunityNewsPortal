from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import news
from django.contrib import auth


class newsform(forms.ModelForm):

	class Meta:
		model = news
		fields = ('heading', 'upvote')
		widgets = { 'heading': forms.TextInput(attrs={'size': 60})}
		#widgets = { 'upvote': forms.TextInput(attrs={'size': 10})}