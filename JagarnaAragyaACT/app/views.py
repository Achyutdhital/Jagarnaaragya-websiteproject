from django.shortcuts import render, HttpResponse,get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from . models import (Slider,
                      AboutUs,
                      ManagingDirector,
                      TeamMemeber,
                      Blog,
                      Gallery,
                      Contact,
                      CustomerQuery,
                      Videos,
                      Notice
                    )


def custom_404_view(request, exception):
    return render(request, 'app/404.html')


class IndexListView(generic.ListView):
    model= Slider
    template_name='app/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexListView,self).get_context_data(*args, **kwargs)
        context['sliders']= Slider.objects.all()
        context['aboutus']= AboutUs.objects.first()
        context['messagefromMD'] = ManagingDirector.objects.first()
        context['teammembers']= TeamMemeber.objects.all().order_by('order')[:4]
        context['blogs'] = Blog.objects.all()[:3]
        return context
    

def indexcustomer(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject= request.POST['subject']
        message = request.POST['message']
        customer_query= CustomerQuery(fullname = name, subject= subject, email=email, message= message)
        customer_query.save()
        messages.info(request,'Query Submitted Sucessfully !')
        return redirect('index')
    return redirect("index")
    

class AboutView(generic.ListView):
    model= AboutUs
    template_name='app/about.html'
    def get_context_data(self, *args, **kwargs):
        context = super(AboutView,self).get_context_data(*args, **kwargs)
        context['aboutus']= AboutUs.objects.first()
        context['teammembers'] = TeamMemeber.objects.all().order_by('order')[:4]
        return context


class BlogListView(generic.ListView):
    model = Blog
    template_name ='app/causes.html'
    context_object_name ='blogs'


class BlodDetailView(generic.DetailView):
    model= Blog
    template_name ='app/blog-details.html'
    slug_field = 'act_slug'
    slug_url_kwarg = 'act_slug'
    def get_context_data(self, *args, **kwargs):
        context = super(BlodDetailView,self).get_context_data(*args, **kwargs)
        context['blogdetail'] = get_object_or_404(Blog, act_slug=self.kwargs['act_slug'])
        context['blogs']= Blog.objects.all().order_by('-id')[:6]
        return context


class NoticeView(generic.ListView):
    model= Notice
    template_name='app/notice.html'
    context_object_name ='allnotice'


class NoticeDetailsView(generic.DetailView):
    model= Notice
    template_name ='app/notice-details.html'
    slug_field = 'notic_slug'
    slug_url_kwarg = 'notic_slug'
    def get_context_data(self, *args, **kwargs):
        context = super(NoticeDetailsView,self).get_context_data(*args, **kwargs)
        context['noticedetails'] = get_object_or_404(Notice, notic_slug=self.kwargs['notic_slug'])
        return context



class TeamListView(generic.ListView):
    model = TeamMemeber
    template_name= 'app/team.html'
    context_object_name ='teammembers'


class GallerView(generic.ListView):
    model = Gallery
    context_object_name='gallery'
    template_name ='app/gallery.html'


class VideoGallery(generic.ListView):
    model= Videos
    context_object_name= 'videos'
    template_name="app/videogallery.html"


def contact(request):
    contact_info  = Contact.objects.first()
    return render(request,'app/contact.html',{'contactinfo':contact_info})


def customerquery(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject= request.POST['subject']
        message = request.POST['message']
        customer_query= CustomerQuery(fullname = name, subject= subject, email=email, message= message)
        customer_query.save()
        messages.info(request,'Query Submitted Sucessfully !')
        return redirect('contact')
    return redirect("contact")