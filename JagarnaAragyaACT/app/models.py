from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

class Slider(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='sliderimage/')
    order_no = models.PositiveIntegerField()
    class Meta:
        ordering = ['-id',]
    

class AboutUs(models.Model):
    title  = models.CharField(max_length=150)
    image = models.ImageField(upload_to='aboutimage/')
    image1= models.ImageField(upload_to='aboutimage/')
    discriptions =RichTextField()
    class Meta:
        ordering = ['-id',]
    
    def __str__(self):
        return self.title


class ManagingDirector(models.Model):
    name = models.CharField(max_length=150)
    position= models.CharField(max_length=150)
    image= models.ImageField(upload_to='mdimage/')
    message= RichTextField()
   

    class Meta:
        ordering =['-id',]

     
class Blog(models.Model):
    blog_title  = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blogimages/')
    created_date = models.DateField(auto_now_add=True)
    discriptions = RichTextField()
    act_slug = AutoSlugField(populate_from = 'blog_title', unique=True, default=None)

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.blog_title
    
class TeamMemeber(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='teamimage/')
    position = models.CharField(max_length=150)
    fbUrl= models.URLField(null=True, blank=True)
    instaUrl = models.URLField(null=True, blank=True)
    twUrl = models.URLField(null=True, blank=True)
    order= models.PositiveIntegerField()
    class Meta:
        ordering =  ['id',]

    def __str__(self):
        return self.name
    

class Gallery(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='galleryimage/')

    class Meta:
        ordering = ['-id',]
    


class Notice(models.Model):
    title  = models.CharField(max_length=250)
    image = models.ImageField(upload_to='noticeimages/')
    created_date = models.DateField(auto_now_add=True)
    discriptions = RichTextField()
    notic_slug = AutoSlugField(populate_from = 'title', unique=True, default=None)

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    location = models.TextField()
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    tel_number = models.PositiveIntegerField(null=True, blank=True)
    fbUrl= models.URLField(null=True, blank=True)
    twUrl = models.URLField(null=True, blank=True)
    instaUrl = models.URLField(null=True, blank=True)
    ybUrl= models.URLField(null=True, blank=True)
    class Meta:
        ordering =['-id',]

   

class CustomerQuery(models.Model):
    fullname = models.CharField(max_length=150)
    subject= models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()


    class Meta:
        ordering =['-id',]

    def __str__(self):
        return self.fullname


class Videos(models.Model):
    video_title = models.CharField(max_length=150, null=True, blank=True)
    video_url= models.URLField()
    
    class Meta:
        ordering =['-id',]

    def __str__(self):
        return self.video_title


