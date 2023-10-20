from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta: 
        verbose_name_plural= "Categories"

    def __str__(self) -> str:
        return self.name


    
class Blog(models.Model):
    category = models.ForeignKey(Category, null= True, on_delete=models.SET_NULL)
    
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog-images", blank=True, null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    is_home  = models.BooleanField(default=False)

    sevilenler = models.ManyToManyField(User,related_name="sevilenler",)
    sevilmeyenler = models.ManyToManyField(User, related_name="sevilmeyenler")
    
    User = models.ForeignKey(User,null= True , on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Yorum(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    Blog= models.ForeignKey(Blog,on_delete=models.CASCADE,null=True)

    content = models.TextField()
    createddate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content


