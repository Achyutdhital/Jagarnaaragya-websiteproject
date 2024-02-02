from django.urls import path
from . import views
from . views import (IndexListView,
                     TeamListView,
                     BlogListView,
                     AboutView,
                     BlodDetailView,
                     GallerView,
                     VideoGallery,
                     NoticeView,
                     NoticeDetailsView
                     )



urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('blog', BlogListView.as_view(), name='blog'),
    path('blog/<slug:act_slug>', BlodDetailView.as_view(), name='blogdetail'),
    path('team', TeamListView.as_view(), name='team'),
    path('contact', views.contact, name='contact'),
    path('customer-query', views.customerquery, name='customer_query'),
    path('gallery/image-gallery', GallerView.as_view(), name='gallery'),
    path('gallery/video-gallery', VideoGallery.as_view(), name='video_gallery'),
    path('notice', NoticeView.as_view(), name='notice'),
    path('notice/<slug:notic_slug>', NoticeDetailsView.as_view(), name='noticedeatils'),
    path('customer-queries', views.indexcustomer, name='index_customer'),
    
]