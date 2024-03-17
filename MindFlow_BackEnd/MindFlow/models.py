from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)  # Add this line

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']

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