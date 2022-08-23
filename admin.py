from django.contrib import admin
from testapp.models import Customer
from testapp.models import MyVideos
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display=['uid','name','dob','gender','email','password','mobile']

class VideoAdmin(admin.ModelAdmin):
    list_display=['title','brand']

admin.site.register(MyVideos,VideoAdmin)
admin.site.register(Customer,UsersAdmin)