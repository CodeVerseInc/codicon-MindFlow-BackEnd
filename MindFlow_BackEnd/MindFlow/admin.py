from django.contrib import admin 
from .models import Users, Profile, Post, Comments

# Register your models here.  
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):  
    fields = ['email', 'username', 'password'] 
    list_display = ['email', 'username', 'password'] 

@admin.register(Profile)    
class ProfileAdmin(admin.ModelAdmin):  
    fields = ['user', 'profile_photo', 'username_fk', 'description'] 
    list_display = ['user', 'profile_photo', 'username_fk', 'description'] 

@admin.register(Post)    
class PostAdmin(admin.ModelAdmin): 
    fields = ['profile_fk', 'title', 'content'] 
    list_display = ['profile_fk', 'title', 'content'] 

@admin.register(Comments)     
class CommentsAdmin(admin.ModelAdmin): 
    fields = ['profile_fk', 'content'] 
    list_display = ['profile_fk', 'content']

