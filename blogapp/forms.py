from django import forms
from .models import Category, Blog ,Yorum
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserForm(UserCreationForm):
   class Meta:
      model = User
      fields = ("username","email","password1","password2")

class CategoryForm(forms.ModelForm):
   class Meta:
      model = Category
      fields= "__all__"

class BlogForm(forms.ModelForm):
   class Meta:
      model = Blog
      fields = ["title","description","image","is_active","is_home","category"]

      image = forms.FileInput()

class LoginForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={
      "pleaceholder": "Your username",
      "class" : "form-control "
   }))
   password = forms.CharField(widget=forms.PasswordInput(attrs={
      "pleaceholder": "Your password",
      "class" : "form-control"
   }))

class YorumForm(forms.ModelForm):
   class Meta: 
      model = Yorum
      fields = ['content']