from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.urls import path
from device import views
from device.views import phonebuy
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('device/', views.device, name='device'),
    path('tabCompare/', views.tabCompare, name='tabCompare'),
    path('watch/', views.watch, name='watch'),
    path('phoneCompare/', views.phoneCompare, name='phoneCompare'),
    path('iphone/', views.iphone, name='iphone'),
    path('Samsung/', views.Samsung, name='Samsung'),
    path('samsungoutput/', views.samsungoutput, name='samsungoutput'),
    path('ipad/', views.ipad, name='ipad'),
    path('ipadoutput/', views.ipadoutput, name='ipadoutput'),
    path('samsungTab/', views.samsungTab, name='samsungTab'),
    path('samsungtaboutput/', views.samsungtaboutput, name='samsungtaboutput'),
    path('iphone/', views.iphone, name='iphone'),
    path('iphoneoutput/', views.iphoneoutput, name='iphoneoutput'),
    path('phonebuy/', views.phonebuy, name='phonebuy'),
    path('tabbuy/', views.tabbuy, name='tabbuy'),
    path('watchbuy/', views.watchbuy, name='watchbuy'),
    path('phonePayment/', views.phonePayment, name='phonePayment'),
    path('watchCompare/', views.watchCompare, name='watchCompare'),
    path('applewatch/', views.applewatch, name='applewatch'),
    path('applewatchoutput/', views.applewatchoutput, name='applewatchoutput'),
    path('samsungwatch/', views.samsungwatch, name='samsungwatch'),
    path('samsungwatchoutput/', views.samsungwatchoutput, name='samsungwatchoutput'),
    path('shipment/', views.shipment, name='shipment'),
    path('thankyou/', views.thankyou, name='thankyou'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
