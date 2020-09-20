from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model


# admin.site.unregister(User)
# admin.site.unregister(Group)
admin.site.site_header = 'Authentic Tours Admin'
admin.site.site_title = 'Authentic Admin'
admin.site.index_title = 'Welcome to Authentic Tours Admin'

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message')
    list_filter = ('date_created',)

class CommunityAdmin(admin.ModelAdmin):
    list_display = ('community_name', 'region', 'description', 'duration', 'image','date_created')
    list_filter = ('date_created',)    

class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'description', 'country', 'image','date_created')
    list_filter = ('date_created',)  


class PackageAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'description', 'destination', 'country', 'duration', 'Price','image','date_created')
    list_filter = ('date_created',)
    
    
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','date_created','adult','kids','message')
    list_filter = ('date_created',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'poststatus', 'created_on')
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('title',)}
    
    
admin.site.register(Message,MessageAdmin)
admin.site.register(Package,PackageAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Community,CommunityAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(Post,PostAdmin)