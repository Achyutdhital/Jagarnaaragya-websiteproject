from django.contrib import admin
from . models import Slider,AboutUs,TeamMemeber,Gallery,Notice,Contact,CustomerQuery,Blog,ManagingDirector,Videos


admin.site.site_header = 'Jagarna Aragya Admin Panel'        
admin.site.index_title = 'Jagarna Aragya'                
admin.site.site_title = 'Welcome to Jagarna Aragya admin panel' 


class SliderAdmin(admin.ModelAdmin):
    model:Slider
    list_display =['title','image']
admin.site.register(Slider, SliderAdmin)


class AboutUsAdmin(admin.ModelAdmin):
    model:AboutUs
    list_display =['title', 'image']
admin.site.register(AboutUs, AboutUsAdmin)



class ManagingDirectorAdmin(admin.ModelAdmin):
    model:ManagingDirector
    list_display =['name','position','image']
admin.site.register(ManagingDirector, ManagingDirectorAdmin)

class BlogAdmin(admin.ModelAdmin):
    model:Blog
    list_display =['blog_title','image','created_date']
admin.site.register(Blog,BlogAdmin)

class TeamMemeberAdmin(admin.ModelAdmin):
    model:TeamMemeber
    list_display =['name','image','position','order']
admin.site.register(TeamMemeber, TeamMemeberAdmin)

class GalleryAdmin(admin.ModelAdmin):
    model:Gallery
    list_display =['title','image']
admin.site.register(Gallery, GalleryAdmin)

class NoticeAdmin(admin.ModelAdmin):
    model:Notice
    list_display =['title','image','created_date']
admin.site.register(Notice, NoticeAdmin)


class ContactAdmin(admin.ModelAdmin):
    model :Contact
    list_display = ['location','phone_number','email']
admin.site.register(Contact, ContactAdmin)

class CustomerQueryAdmin(admin.ModelAdmin):
    model:CustomerQuery
    list_display =['fullname','email']
admin.site.register(CustomerQuery, CustomerQueryAdmin)


class VideosAdmin(admin.ModelAdmin):
    model : Videos
    list_display= ['video_title','video_url']
admin.site.register(Videos,VideosAdmin)