from . models import Contact,AboutUs

def contact_info(request):
    contactinfo = Contact.objects.first()
    return ({
        'contactinfo':contactinfo
    })

def about_us(request):
    aboutus = AboutUs.objects.first()
    return ({
        'aboutus':aboutus
    })