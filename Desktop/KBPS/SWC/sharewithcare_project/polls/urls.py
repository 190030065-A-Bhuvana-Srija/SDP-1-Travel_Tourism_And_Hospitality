from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    #example==/polls/
    #path('',views.index,name='index'),
    #example== /polls/5/
    #path('<int:question_id>/',views.results,name='results'),
    #path('index2/',views.index2,name='index2'),
    #path('index3/',views.index3,name='index3'),
    path('signup/',views.signup,name='signup'),
    path('signupfarm/',views.signupfarm,name='signupfarm'),
#    path('signup/enter/',views.UpAction,name='enterup'),
    path('login/',views.login,name='login'),
  #  path('login/enter/',views.inAction,name='enterin'),
    path('sendmail/',views.send_email,name='email'),
    path('buy/',views.buy,name='buy'),
    path('sell/',views.sell,name='sell'),
    path('forgtpswrd/',views.forgtpswrd,name='forgtpswrd'),
    path('buyAndsell/',views.buyAndSell,name='buyAndsell'),
    path('gallery/',views.gallery,name="gallery"),
    path('home/',views.home,name='home'),
    path('loginfarm/',views.loginfarm,name='loginfarm'),
    path('buyfarm/',views.buyfarm,name='buyfarm'),
    path('forgtpswrdfarm/',views.forgtpswrdfarm,name='forgtpass'),
    path('checkcart/',views.checkcart,name="chechcart"),
     path('checkcartfarm/',views.checkcartfarm,name="chechcartfarm"),
    path('buyerbuy/',views.buyerbuy,name="buyerbuy"),
    path('se/',views.se,name="Se"),
    path('contus/',views.contus,name="contus"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('feedback/',views.feed,name="feedback"),
    path('sugg/',views.sugg,name="sugg"),
    path('upload/',views.image_upload_view,name="uplad"),
  #  path('showimg',views.showimage,name="showimg"),
   
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    