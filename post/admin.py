from audioop import reverse
from django.contrib import admin
from post.models import Post,ProfileUser
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','created']
    ist_display_links=['id','title']
    search_fields =['title','description']
    list_filter = ['created']

class ProfileUserAdmin(admin.ModelAdmin):
    list_display=['id','user','created']
    ist_display_links=['id','title']
    search_fields =['user']
    list_filter = ['created']

admin.site.register(Post)
admin.site.register(ProfileUser)

