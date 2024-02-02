from django.shortcuts import render,HttpResponse, HttpResponseRedirect,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . decorators import login_required
from django.contrib import messages
from django.contrib import auth
from . new_file_handler import validate_file
from app.models import *
import re
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string,get_template


def login(request):
    try:
        if request.user.is_authenticated:
            return render(request,'dashboard/index.html')

        if request.method =="POST":
            username = request.POST['username']
            password = request.POST['password']
            user_obj = User.objects.filter(username= username)
            if not user_obj.exists():
                messages.error(request,"Invalid username...")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                
            
            user_obj = authenticate(username=username, password=password)
            if user_obj and user_obj.is_superuser:
                auth.login(request, user_obj)
                return redirect('dashboard:index')
            
            messages.error(request,'Inavlid Password')
            return redirect('dashboard:login')
            
        return render(request,'dashboard/login.html')
            

    except Exception as e:
        # print(e)
        messages.error(request,'something wrong...')
        return redirect('dashboard:login')


@login_required
def index(request):
    news = Blog.objects.all()[:5]
    press = Notice.objects.all()[:5]
    return render(request,'dashboard/index.html',{'news':news,
                                                  'press':press
                                                  })


@login_required
def managingdirecory(request):
    mdmessage= ManagingDirector.objects.first()
    return render(request,'dashboard/md.html',{'mdmessage':mdmessage})

@login_required
def udate_md(request):
    if request.method=="POST":
        id= request.POST['id']
        md = ManagingDirector.objects.get(id= id)
        md.name= request.POST['name']
        md.position = request.POST['position']
        md.image = request.FILES['image']
        md.message = request.POST['message']
        md.save()
        messages.info(request,'Update successfully !')
        return redirect('dashboard:mdmessage')
    return redirect('dashboard:mdmessage')

@login_required
def userlogout(request):
    auth.logout(request)
    messages.info(request,"logout successfully..")
    return redirect('dashboard:login')


@login_required
def aboutus(request):
    if request.method =="POST":
        id= request.POST['id']
        aboutus = AboutUs.objects.get(id= id)
        aboutus.title = request.POST['title']
        image_file= request.FILES['image']
        if image_file is not None:
            aboutus.image = request.FILES['image']
        aboutus.discriptions = request.POST['discription']
        aboutus.save()
        print(request.FILES['image'])
        return HttpResponse("success")

    aboutus = AboutUs.objects.first()
    return render(request,'dashboard/about.html',{'aboutdata':aboutus})

@login_required
def blogs(request):
    blogs = Blog.objects.all()
    return render(request,'dashboard/blog.html',{'blogs':blogs})

@login_required
def createblog(request):
    if request.method == "POST":
        title = request.POST['title']
        image = request.FILES['image']
        discriptions = request.POST['discription']
        newblog = Blog.objects.create(blog_title=title, image=image, discriptions= discriptions)
        newblog.save()
        messages.success(request,'New blog added Successfully !')
        return redirect('dashboard:blog')
    return render(request,'dashboard/blogcreate.html')


@login_required
def viewblog(request, slug):
    blog = Blog.objects.get(act_slug= slug)
    return render(request,'dashboard/blogview.html',{'blogsdata':blog})


@login_required
def blogupdate(request, slug):
    if request.method =="POST":
        blog= Blog.objects.get(act_slug= slug)
        blog.blog_title = request.POST['title']
        blog.image= request.FILES['image']
        blog.discriptions = request.POST['discription']
        blog.save()
        messages.info(request, "Update successfully !")
        return redirect('dashboard:blog')
    relatedblog= Blog.objects.get(act_slug= slug)
    return render(request, 'dashboard/blogupdate.html',{'blogdata':relatedblog})

@login_required
def delete_blog(request, slug):
    blog= Blog.objects.get(act_slug= slug)
    blog.delete()
    messages.warning(request,"Delete Successfully !")
    return redirect('dashboard:blog')

@login_required
def notice(request):
    allnotice= Notice.objects.all()
    return render(request,'dashboard/notice.html',{'allnotice':allnotice})

@login_required
def notice_create(request):
    if request.method =="POST":
        title = request.POST['title']
        image = request.FILES['image']
        discriptions= request.POST['discription']
        new_notice = Notice.objects.create(title=title, image= image, discriptions =discriptions)
        new_notice.save()
        messages.success(request,'New Notice Added Successfully !')
        return redirect('dashboard:notice')
    return render(request,'dashboard/notice_create_from.html')


@login_required
def notice_view(request, slug):
    related_notice = Notice.objects.get(notic_slug=slug)
    return render(request,'dashboard/noticeview.html',{'noticedata':related_notice})

@login_required
def notice_edit(request, slug):
    relatednotice= Notice.objects.get(notic_slug= slug)
    if request.method =="POST":
        relatednotice.title = request.POST['title']
        relatednotice.image = request.FILES['image']
        relatednotice.discriptions = request.POST['discription']
        relatednotice.save()
        messages.info(request,"Notice Update Successfully !")
        return redirect('dashboard:notice')
    return render(request,'dashboard/noticeupdate.html',{'relate_notice':relatednotice})

@login_required
def delete_notice(request, slug):
    notice= Notice.objects.get(notic_slug= slug)
    notice.delete()
    messages.warning(request,"Delete Successfully !")
    return redirect('dashboard:notice')


@login_required
def team_members(request):
    members = TeamMemeber.objects.all()
    return render(request,'dashboard/executivemember.html',{'teammembers':members})

@login_required
def add_new_member(request):
    if request.method=="POST":
        name =request.POST['name']
        image = request.FILES['image']
        position= request.POST['position']
        new_member = TeamMemeber.objects.create(name= name, image=image, position=position)
        new_member.save()
        messages.success(request,"New member added Successfully !")
        return redirect('dashboard:team_members')
    return redirect('dashboard:team_members')

@login_required
def update_member(request):
    if request.method == "POST":
        id = request.POST['memberid']
        member= TeamMemeber.objects.get(id =id)
        member.name =request.POST['name']
        member.image = request.FILES['image']
        member.position= request.POST['position']
        member.save()
        messages.success(request,"Update Successfully !")
        return redirect('dashboard:team_members')
    return redirect("dashboard:team_members")

@login_required
def delete_member(request):
    id= request.POST['memberid']
    member= TeamMemeber.objects.get(id= id)
    member.delete()
    messages.warning(request,"Member Delete Successfully !")
    return redirect('dashboard:team_members')


@login_required
def contact(request):
    contactinfo= Contact.objects.first()
    if request.method=="POST":
        id = request.POST['id']
        contact_info = Contact.objects.get(id=id)
        contact_info.email = request.POST['email']
        contact_number=request.POST['phone']
        phone_number=r'^(97|98)\d{8}$'
        if not re.match(phone_number, contact_number):
            messages.warning(request,'Phone number Invalid ! Phone number starts with 97 or 98 and exactly 10 digits.')
            return redirect('dashboard:contact')
        contact_info.phone_number= request.POST['phone']
        contact_info.location = request.POST['location']
        contact_info.tel_number = request.POST['teliphone']
        contact_info.fbUrl = request.POST['fburl']
        contact_info.instaUrl= request.POST['insta']
        contact_info.twUrl = request.POST['twiter']
        contact_info.ybUrl = request.POST['ybUrl']
        contact_info.save()
        messages.success(request,'Update Successfully !')
        return redirect('dashboard:contact')
    return render(request,'dashboard/contact.html',{'contactinfo':contactinfo})

@login_required
def gallery(request):
    allimage = Gallery.objects.all()
    return render(request,'dashboard/galleryedit.html',{'images':allimage})

@login_required
def delete_image(request):
    if request.method =="POST":
        imageid = request.POST['id']
        image= Gallery.objects.get(id=imageid)
        image.delete()
        messages.success(request,"Image delete Successully !")
        return redirect('dashboard:gallery')
    return redirect('dashboard:gallery')

@login_required
def addnewimage(request):
    if request.method == "POST":
        title = request.POST['title']
        image= request.FILES['image']
        newimage = Gallery.objects.create(title=title, image=image)
        newimage.save()
        messages.success(request,'New image added Successfully !')
        return redirect('dashboard:gallery')
    return redirect('dashboard:gallery')


@login_required
def videogallery(request):
    if request.method == "POST":
        video_url = request.POST['url']
        video_title = request.POST['title']
        obj = Videos(video_url= video_url,
                    video_title =video_title
                    )
        obj.save()
        messages.success(request,"video added successfully...")
        return redirect("dashboard:videogallery")
    else:
        videos = Videos.objects.all()
        return render(request,'dashboard/video.html',{'allvideos':videos})


@login_required
def delete_video(request):
    if request.method == "POST":
        id = request.POST['videoid']
        video = Videos.objects.get(id = id)
        video.delete()
        messages.success(request,"video deleted successfully...")
        return redirect("dashboard:videogallery")



@login_required
def bannarimage(request):
    bannarimage = Slider.objects.all().order_by('-order_no')
    return render(request, 'dashboard/bannarimage.html',{'bannar_images':bannarimage})

@login_required
def addbannarimage(request):
    if request.method == "POST":
        title = request.POST['title']
        image= request.FILES['image']
        ordernumber= request.POST['ordernumber']
        newimage= Slider.objects.create(image=image,title= title, order_no = ordernumber)
        newimage.save()
        messages.success(request,"New image added Successfully !")
        return redirect("dashboard:bannarimage")
    return redirect("dashboard:bannarimage")

@login_required
def deletebannarimage(request):
    if request.method == "POST":
        id = request.POST['id']
        newimage= Slider.objects.get(id=id)
        newimage.delete()
        messages.success(request,"Image deleted Successfully !")
        return redirect("dashboard:bannarimage")
    return redirect("dashboard:bannarimage")


@login_required
def customerquery(request):
    if request.method == "POST":
        id= request.POST['queriesid']
        queries= CustomerQuery.objects.get(id=id)
        subject = request.POST['subject']
        message= request.POST['messages']
        details ={'subject':subject,
                    'message':message
                    }
        
        message = get_template('dashboard/queries.html').render(details)
        email_from = settings.EMAIL_HOST_USER
        email_to = queries.email
        recipient_list = [email_to]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request,'Message sent sucessfully !')
        return redirect("dashboard:customer-queries")
    customerqueries= CustomerQuery.objects.all().order_by('-id')
    return render(request,'dashboard/customerquery.html',{'customer_queries':customerqueries})


@login_required
def delete_quries(request):
    if request.method=="POST":
        queriesId = request.POST['queiresid']
        customerqueries= CustomerQuery.objects.get(id= queriesId)
        customerqueries.delete()
        messages.info(request,"Queries Deleted Succsefully !")
        return redirect("dashboard:customer-queries")
    return redirect("dashboard:customer-queries")
    