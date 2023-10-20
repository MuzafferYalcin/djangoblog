from django.shortcuts import get_object_or_404, redirect, render
from blogapp.models import Blog,Category,Yorum,User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import BlogForm,UserForm ,LoginForm , YorumForm



def index(request):
   blogs= Blog.objects.all()
   return render(request,"blog/blogs.html",{"blogs":blogs})


def blog_detail(request,id):
   blog = Blog.objects.get(id=id)
   user = User.objects.get(id=blog.User.id)
   yorums = Yorum.objects.filter(Blog = blog).order_by("-createddate")
   if request.user.is_authenticated:
      if request.method == 'POST':
         form = YorumForm(request.POST)
         if form.is_valid():
            yorum =  form.save(commit=False)
            yorum.User = request.user
            yorum.Blog = blog
            yorum.save()
            
            return redirect("blog-details", id = id)
      else:
         form = YorumForm()
         x = ""
   else:
      x = "giriş yap"
      form = YorumForm()
   
   return render(request,"blog/blog-detail.html",{"blog":blog,"yorums":yorums,"form":form, "user":user,"x":x})

def signup(request):
   if request.method == 'POST':
      signform = UserForm(request.POST)
      if signform.is_valid():
         signform.save()
         return redirect("index")
   else:
      signform = UserForm()
   print(type(signform))
   return render(request,"blog/signup.html",{"form":signform})

def logoutuser(request):
   logout(request)
   return redirect("index")

def login(request):
   if request.method == "POST":
      loginForm = LoginForm(request.POST)
      
   return render(request, "blog/login.html")

@login_required      
def newblog(request):
   if request.method == "POST":
      form = BlogForm(request.POST, request.FILES)
      if form.is_valid():
         item = form.save(commit= False)
         item.User = request.user
         item.save()
         return redirect('blog-details', id=item.id)
   else:
      form = BlogForm()
   return render(request,'blog/newblog.html',{"form":form})


@login_required   
def myblogs(request):
   blogs = Blog.objects.filter(User = request.user)
 
   return render(request,"blog/myblogs.html",{"blogs": blogs})

@login_required   
def myfavorites(request):
   blogs = Blog.objects.filter(sevilenler = request.user)
   
   return render(request,'blog/sevilenler.html',{"blogs":blogs})

@login_required   
def begen(request,blogid):
   blog = Blog.objects.get(id = blogid)
   if request.method == 'POST':
      if not blog.sevilenler == request.user:
         blog.sevilenler.add(request.user)
         return redirect("index")

   return redirect("index")

@login_required   
def begenme(request,blogid):
   blog = Blog.objects.get(id = blogid)
   if blog.sevilenler.contains(request.user):
      blog.sevilenler.remove(request.user)
 
   return redirect("sevilenler")

