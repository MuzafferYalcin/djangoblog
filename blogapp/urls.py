from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm 

from . import views


urlpatterns = [
    path("login/",auth_views.LoginView.as_view(template_name="blog/login.html",authentication_form = LoginForm),name="login"),
    
    path("",views.index,name="index"),
    
    path("blog-detail/<int:id>",views.blog_detail,name="blog-details"),
    
    path("signup",views.signup,name="signup"),
    
    path("newblog",views.newblog,name="newblog"),

    path("myblogs",views.myblogs,name="myblogs"),

    path("sevilenler",views.myfavorites,name="sevilenler"),

    path("addsevilen/<int:blogid>", views.begen, name="begen"),

    path("deletesevilen/<int:blogid>", views.begenme, name="begenme"),

    path("logout",views.logoutuser, name="logout"),

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)