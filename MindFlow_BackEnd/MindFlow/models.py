from django.contrib.auth.models import User
from django.db import models

# Create your models here. 
# Solucionar problema de herencia de User
class Users(models.Model):   
    email = models.EmailField(unique=True) 
    username = models.CharField(max_length=100, unique=True)  
    password = models.CharField(max_length=128, null=False)  

    class Meta: 
        db_table = 'users' 
        verbose_name = 'User'
        verbose_name_plural = 'Users' 
        ordering = ['id'] 
        unique_together = ['email', 'username', 'password'] 
         
    def __str__(self): 
        return self.username
  

class Profile(models.Model):  
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='profile') 
    profile_photo = models.URLField(max_length=500)   
    username_fk = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='profiles') 
    description = models.TextField(max_length=500)
       
    class Meta: 
        db_table = 'profile' 
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles' 
        ordering = ['id'] 
         
    def __str__(self): 
        return self.user.username

class Post(models.Model): 
    profile_fk = models.ForeignKey(Profile, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100) 
    content = models.TextField(max_length=500)  
     
    class Meta: 
        db_table = 'post' 
        verbose_name = 'Post'
        verbose_name_plural = 'Posts' 
        ordering = ['id'] 
         
    def __str__(self): 
        return self.title.content

   
class Comments(models.Model): 
    profile_fk = models.ForeignKey(Profile, on_delete=models.CASCADE) 
    post_fk = models.ForeignKey(Post, on_delete=models.CASCADE) 
    content = models.TextField(max_length=500) 
     
    class Meta: 
        db_table = 'comments' 
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments' 
        ordering = ['id'] 
         
    def __str__(self): 
        return self.content