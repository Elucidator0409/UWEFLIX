"""uwe_flix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView 

from django.views.generic import TemplateView
from django.conf.urls.static import static

from booking.views import home, show_index, movie_details,reserve_seat,payment_gateway,payment_confirmation


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    
    
    re_path(r'^$', home, name='home'),
    re_path(r'^booking/$', show_index, name='booking'),
    re_path(r'^booking/seatchoice/(?P<show_id>\d+)/$', reserve_seat, name='reserve_seat'),
    re_path(r"login$", LoginView.as_view(template_name="signin.html"), name="player_login"),
    
    re_path(r'^booking/(?P<movie_id>\d+)/$', movie_details, name='movie_details'),
    re_path(r'^booking/payment/$', payment_gateway, name='payment_gateway'),
    re_path(r'^booking/payment_confirmation/$', payment_confirmation, name='payment_confirmation'),
    re_path(r'^booking/payment/seatnotfound.html$', TemplateView.as_view(template_name="seatnotfound.html"), name='seatnotfound'),
    re_path(r'^booking/payment_confirmation/seatconflict.html$', TemplateView.as_view(template_name="seatconflict.html"), name='seatconflict'),
    
   
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #all values set in settings.py
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)