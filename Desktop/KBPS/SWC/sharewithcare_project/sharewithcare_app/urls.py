import profile

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import models
# we need to map each url to it's view (views.py)
from . import views
from .views import *

urlpatterns = [
    # path('', views.home),
    # path() contains 4 args - urlpath, urlview, variablenumofargs(using a dict), name
    # import the view too
    # . meands the current path
    path('index', index),
    path('sharewithcare_app', index),
    path('', index),
    path('rawproducts', rawproducts),
    path('listofinterproducts', listofinterproducts),
    path('interproducts', interproducts),
    path('endproducts', endproducts),
    path('addrawproducts', addrawproducts),
    path('addinterproducts', addinterproducts),
    path('addendproducts', addendproducts),
    path('cart', cart),
    path('pay', pay),
    path('Sweets', Sweets),
    path('Beverages', Beverages),
    path('Kulfis', Kulfis),
    path('Cakes', Cakes),
    path('Dairy', Dairy),
    path('Curd', curd),
    path('Paneer', paneer),
    path('Ghee', ghee),
    path('Butter', butter),
    path('Cream', cream),
    path('bestsellers', bestsellers),
    path('coupon', luck),
    path('logout', logout),
    path('ordertrack', ordertrack),
    path('progress', progress),
    path('luck', luck),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)