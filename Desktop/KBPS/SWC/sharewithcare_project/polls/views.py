from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, table, seller, verif, farmer, corporate, cart, feedback
from django.template import loader
from django.core.mail import send_mail, BadHeaderError
import smtplib
import string
from polls.forms import sellerform
from django.views.decorators.csrf import csrf_protect
from django.conf import settings


### admin page   username=varun  pass=9494868523

# Create your views here.

# as you add any function here update in urls to connect it
# this urls map to needed page by address 


# Each view is responsible for doing one of two things:
#  returning an HttpResponse object containing the content for the requested page, 
# or raising an exception such as Http404.

# to add these new functionalities we alo need to add at urls.py in polls

# this is connecting views to database see this carefully
# to use db tables import from .models and type table name

#: the page’s design is hard-coded in the view. 
# If you want to change the way the page looks,
#  you’ll have to edit this Python code. So let’s use Django’s 
# template system to separate the design from Python by creating a
#  template that the view can use.   
# so create a templatess directory in polls directory.

# Your project’s TEMPLATES setting describes
# how Django will load and render templates

# . In other words, your template should be at polls/templates/polls/index.html.
#  Because of how the app_directories template loader works as described above,
#  you can refer to this template within Django as polls/index.html.

# because the html is fixed by using this king of above views we are are 
# using templates in this way this needs loader and 
#  The context is a dictionary mapping template variable names to Python objects.

# if we need not to loader to import then we can use this  


## this function will take sign up needed informatioin from ""farmers""  and validate with the requirements
## and after validation is succesfull and satisfied  it adds into the data base tables

def signupfarm(request):
    if request.GET:
        na = request.GET
        if "cancel" in na:
            return render(request, 'polls/signupfarm.html')
        name = na['who']
        pswrd = na['pass']
        phn = na['phn']
        ema = na['email']
        ident = na['ident']
        if len(name) == 0 or len(pswrd) == 0 or len(ident) == 0 or len(ema) == 0 or len(phn) != 10:
            return render(request, 'polls/signupfarm.html', {'mssg': "enter the details"})

        try:
            obj = verif.objects.get(user_name=name)
        except:
            return render(request, 'polls/signupfarm.html', {'mssg': "invalid farmer id"})

        if obj.user_id == ident:
            t = farmer(user_name=name, password=pswrd, email=ema, phn=phn)
            t.save()
            return HttpResponseRedirect('/polls/loginfarm/')
            # render(request,'polls/succsesful.html')
        else:
            return render(request, 'polls/signupfarm.html', {'mssg': "invalid farmer id"})
    else:
        return render(request, 'polls/signupfarm.html')


## this function will take sign up needed informatioin  from "" Customers""  and validate with the requirements 
## and after validation is succesfull and satisfied  it adds into the data base tables
def signup(request):
    # if no data is sent is showing error see that
    # print(name)
    # print(request.POST)
    if request.GET:
        na = request.GET
        if "cancel" in na:
            return render(request, 'polls/signup.html')
        name = na['who']
        pswrd = na['pass']
        phn = na['phn']
        ema = na['email']
        # print("entered buyyer email==",ema)
        if len(name) == 0 or len(pswrd) == 0 or len(ema) == 0 or len(phn) != 10:
            # print("in if  ")
            return render(request, 'polls/signup.html', {'mssg': "enter the details"})
            # print("out of if")
        t = table(user_name=name, password=pswrd, email=ema, phn=phn)
        t.save()
        return HttpResponseRedirect('/polls/login/')
        # render(request,'polls/succsesful.html')
    else:
        return render(request, 'polls/signup.html')


## this function will take  login  informatioin from farmers  and validate with the data base that 
## whether this person is a user and if will the password match. if everything passes then it will redirect to buyer and selling page for farmers
nm = "none"
zell = "None"


def loginfarm(request):
    if request.GET:
        na = request.GET
        if "cancel" in na:
            return render(request, 'polls/loginfarm.html')

        name = na['who']
        pswrd = na['pass']
        global nm
        print(nm)
        nm = name
        # nm=name
        print(nm)
        try:
            obj = farmer.objects.get(user_name=name)
        except:
            return render(request, 'polls/loginfarm.html', {'mssg': "invalid password or username"})

        if obj.password == pswrd:
            return redirect('/polls/buyAndsell/')
            # return render(request,'polls/buyAndSell.html',{'name':name})
        else:
            return render(request, 'polls/loginfarm.html', {'mssg': "invalid password or username"})
    else:
        return render(request, 'polls/loginfarm.html')


## this function will take  login  information from customers  and validate with the data base that
## whether this person is a user and if will the password match. if everything passes then it will redirect to buyer and selling page for customers

def login(request):
    if request.GET:
        na = request.GET
        if "cancel" in na:
            return render(request, 'polls/login.html')
        name = na['who']
        pswrd = na['pass']
        global nm
        print(nm)
        nm = name
        try:
            obj = table.objects.get(user_name=name)
        except:
            return render(request, 'polls/login.html', {'mssg': "invalid password or username"})

        if obj.password == pswrd:
            return redirect('/polls/buyerbuy/', name=nm)
        # return render(request,'polls/buyerbuy.html',{'name':nm})
        else:
            return render(request, 'polls/login.html', {'mssg': "invalid password or username"})
    else:
        return render(request, 'polls/login.html')


## this is when customer want to buys and selects the products to buy 
# this will redirect to the appropriate page like page which shows available sellers.
def buyerbuy(request):
    if request.GET:
        na = request.GET
        if 'crop' in na:
            food = na['crop']
            urle = "/polls/buyfarm/?crop=" + food
            return redirect(urle)

    else:
        print(nm)
        return render(request, 'polls/buyerbuy.html', {'name': nm})


## this function is for farmers to gom to selling page
def se(request):
    return render(request, 'polls/sel.html')


# this function is to redirect to the about us page of website
def aboutus(request):
    return render(request, 'polls/Aboutus.html')


### this function is for customers to enter ehat crip they want and it will show the available sellers 
### and based on the available sellersthey can select one and submit it and they have  an option of 
### delivery or add to cart
def buyAndSell(request):
    if request.GET:
        na = request.GET
        print(nm)
        if 'crop' in na:
            obj = seller.objects.order_by().values('crop_name').distinct()
        if 'crop' in na and 'firstname' not in na:
            food = na['crop']
            print(food)
            global zell
            zell = food
            print(zell)
            obj = seller.objects.filter(crop_name=food)
            o = []
            if len(obj) == 0:
                urle = "/polls/buy/?crop=" + food
                return redirect(urle)
            for i in obj:
                a = seller.objects.get(user_name=i)
                o.append(a)
            obj = seller.objects.order_by().values('crop_name').distinct()
            print(o)
            zi = feedback.objects.filter(crop_name=food)
            # print("star",zi)
            star = "None"
            print(zi)
            if len(zi) != 0:
                for i in zi:
                    a = feedback.objects.get(crop_name=i)
                    star = a.rate
            else:
                star = 1
            print(star)
            urle = "/polls/buyfarm/?crop=" + food
            return redirect(urle)
            # return redirect('/polls/buy/',obj=o,item=obj,crop_nm=food,rate=star)
            # return render(request,'polls/buyer.html',{'obj':o,'item':obj,'crop_nm':food,'rate':star})
    else:
        return render(request, 'polls/buyAndSell.html', {'name': nm})


# def inAction(request):
#    if request.method=='GET':

# we can pass object 
# like if the obj=table() return render(request,'polls/buy..',{'user':obj})
# we can send multiple users like users=[user1,user2,...] by replacing {'user': users}

# def send_email(request):
# subject = request.POST.get('subject', '')
# message = request.POST.get('message', '')
# from_email = request.POST.get('from_email', '')
#    subject='hello this mail system is working'
#    message='sent fromm django'
#    from_email='varunakrishna1@gmail.com' 
#    if subject and message and from_email:
#        try:
#            send_mail(subject, message, from_email, ['vikram.g19@iiits.in'],fail_silently=False)
#        except BadHeaderError:
#            return HttpResponse('Invalid header found.')
#        return HttpResponseRedirect('/contact/thanks/')
#    else:
#        # In reality we'd use a form class
#        # to get proper validation errors.
#        return HttpResponse('Make sure all fields are entered and valid.')

# we can alos use  send_mass_mail()  to send mass mails in the aboove also can sen we need to add recepient at reciepent(to) [] list


#### this is for sending notification for sellers to get notified
### when some one buys their product 
### it is via emial

import string


def send_email(request):
    username = "project2wad@gmail.com"
    password = "Wad@project2#"
    smtp_server = "smtp.gmail.com:587"
    email_from = "project2wad@gmail.com"
    email_to = "varunakrishna.k19@iiits.in"

    send_mail(
        "django checkin",
        "hoping nthis is the in body new msg",
        email_from,
        [email_to],
        # ['varunakrishna.k19@iiits.in'],
    )
    return render(request, 'polls/succsesful.html')


zk = "none"


def buy(request):
    if request.GET:
        na = request.GET
        print(na)
        # food=na['crop']
        obj = seller.objects.order_by().values('crop_name').distinct()
        # objects.filter(crop_name=food)
        if 'crop' in na and 'firstname' not in na:
            food = na['crop']
            print(food)
            global zk
            zk = food
            print(zk)
            obj = seller.objects.filter(crop_name=food)
            o = []
            if len(obj) == 0:
                return render(request, 'polls/buyer.html', {'obj': o, 'item': obj, 'crop_nm': food, 'rate': "0",
                                                            'nope': "no seller for the selected product right now!!"})
            for i in obj:
                a = seller.objects.get(user_name=i)
                o.append(a)
            obj = seller.objects.order_by().values('crop_name').distinct()
            print(o)
            zi = feedback.objects.filter(crop_name=food)
            # print("star",zi)
            star = "None"
            print(zi)
            if len(zi) != 0:
                for i in zi:
                    a = feedback.objects.get(crop_name=i)
                    star = a.rate
            else:
                star = 1
            print(star)
            return render(request, 'polls/buyer.html', {'obj': o, 'item': obj, 'crop_nm': food, 'rate': star})
        elif 'crop' not in na and 'firstname' not in na:
            if 'seller' not in na or 'quant' not in na or 'city' not in na or 'phn' not in na:
                return render(request, 'polls/buyer.html', {'item': obj, 'mssg': "enter the details"})
            sell = na['seller']
            name = na['who']
            city = na['city']
            quant = na['quant']
            phn = na['phn']
            email = na['email']
            # global it
            print(zk)
            # print(na['cr'])
            # it=na['cr']
            # it="item"
            oz = seller.objects.filter(crop_name=zk)
            print(oz)
            o = []
            a = seller.objects.get(user_name=sell)
            print(sell)
            print("farmer", a)
            print(a.price_per_kg)
            if len(sell) == 0 or len(city) == 0 or len(phn) != 10:
                return render(request, 'polls/buyer.html', {'item': obj, 'mssg': "enter the details"})
            if 'cart' in na:
                if cart.objects.get(name=name) != "None":
                    print(zk)
                    zz = cart.objects.get(name=name)
                    zz.item = zz.item + " " + zk
                    zz.price = zz.price + " " + str(a.price_per_kg)
                    zz.seller_name = zz.seller_name + " " + sell
                    zz.save()
                    print(zz.seller_name, zz.item)
                    s = zz.seller_name.split(" ")
                    for k in s:
                        print(k + " ")
                else:
                    c = cart(name=name, item=zk, seller_name=sell, price=a.price_per_kg)
                    c.save()
                return render(request, 'polls/buyer.html', {'item': obj, 'mssg': "added to cart"})
            # 'item':obj,
            if farmer.objects.get(user_name=sell) != "None":
                sel_obj = farmer.objects.get(user_name=sell)
                email_to = sel_obj.email
                print(email_to)
                username = "project2wad@gmail.com"
                password = "Wad@project2#"
                smtp_server = "smtp.gmail.com:587"
                email_from = "project2wad@gmail.com"

                send_mail(
                    "you got an order",
                    "your order is for " + name + " at " + city + " and quantity is " + quant + " kg's and his phone number is " + phn,
                    email_from,
                    [email_to],
                )
                return render(request, 'polls/feedbackbuyer.html')
            else:
                return render(request, 'polls/feedbackbuyer.html')
            # return render(request,'polls/feedback.html',{'mssg':"succesful delivery will be there at your home"})
        if 'firstname' in na:
            # print("entered")
            ra = int(na['rate'])
            crop = na['crop']
            if len(crop) == 0 or ra == 0:
                return render(request, 'polls/feedbackbuyer.html', {'mssg': "enter the details"})
            print(ra, crop)
            print("rate", na['rate'])
            if feedback.objects.get(crop_name=crop) != "None":
                rr = feedback.objects.get(crop_name=crop)
                rz = int(rr.rate)
                ra = int((rz + ra) / 2)
                print(ra)
                rr.rate = ra
                rr.save()

            else:
                f = feedback(crop_name=crop, rate=ra)
                f.save()
            # rr=feedback.objects.get(crop_name=crop)
            # rr=int(rr.rate)
            # ra=int((rr+ra)/2)
            # print(ra)
            # f=feedback(crop_name=crop,rate=ra)
            # f.save()
            return render(request, 'polls/buyerbuy.html')
    else:
        obj = seller.objects.order_by().values('crop_name').distinct()
        return render(request, 'polls/buyer.html', {'item': obj})


### this function is for farmers to enter ehat crip they want and it will show the available sellers
### and based on the available sellersthey can select one and submit it and they have  an option of 
### delivery or add to cart
it = "none"


def buyfarm(request):
    if request.GET:
        na = request.GET
        obj = corporate.objects.order_by().values('good_name').distinct()
        # it="crop"
        crop_name = "None"
        print(nm)
        if 'crop' in na and 'firstname' not in na:
            food = na['crop']
            print(food)
            global it
            it = food
            crop_name = food
            print(it)
            obj = corporate.objects.filter(good_name=food)
            o = []
            for i in obj:
                a = corporate.objects.get(company=i)
                o.append(a)
            obj = corporate.objects.order_by().values('good_name').distinct()
            return render(request, 'polls/buyfarm.html', {'obj': o, 'item': obj, 'crop_nm': food, 'name': nm})
        elif 'crop' not in na and 'firstname' not in na:
            if 'seller' not in na or 'city' not in na or 'phn' not in na:
                return render(request, 'polls/buyfarm.html', {'item': obj, 'mssg': "enter the details"})
            sell = na['seller']
            name = na['who']
            city = na['city']
            phn = na['phn']
            email = na['email']
            # global it
            print(it)
            # print(na['cr'])
            # it=na['cr']
            # it="item"
            if len(sell) == 0 or len(city) == 0 or len(phn) != 10:
                return render(request, 'polls/buyfarm.html', {'item': obj, 'mssg': "enter the details"})

            print("idid", it)
            # print(" crop name",crop_name)
            oz = corporate.objects.filter(good_name=it)
            print(oz)
            o = []
            a = corporate.objects.get(company=sell)
            print(sell)
            print("company", a)
            print(a.priceperkg)

            if 'cart' in na:
                if cart.objects.get(name=name) != "None":
                    zz = cart.objects.get(name=name)
                    zz.item = zz.item + " " + it
                    zz.price = zz.price + " " + a.priceperkg
                    zz.seller_name = zz.seller_name + " " + sell
                    zz.save()
                    print(zz.seller_name, zz.item)
                    s = zz.seller_name.split(" ")
                    for k in s:
                        print(k + " ")
                else:
                    c = cart(name=name, item=it, seller_name=sell, price=a.priceperkg)
                    c.save()
                return render(request, 'polls/buyfarm.html', {'item': obj, 'mssg': "added to cart", 'name': nm})
            # 'item':obj,
            if corporate.objects.get(company=sell) != "None":
                sel_obj = corporate.objects.get(company=sell)
                email_to = sel_obj.email
                print(email_to)
                username = "project2wad@gmail.com"
                password = "Wad@project2#"
                smtp_server = "smtp.gmail.com:587"
                email_from = "project2wad@gmail.com"

                send_mail(
                    "you got an order",
                    "your order is for " + name + " at " + city + "  and his phone number is " + phn,
                    email_from,
                    [email_to],
                )
                return render(request, 'polls/feedback.html', {'name': nm})
            else:
                return render(request, 'polls/feedback.html', {'mssg': "succesful delivery will be there at your home"})
        if 'firstname' in na:
            # print("entered")
            ra = int(na['rate'])
            crop = na['crop']
            if len(crop) == 0 or ra == 0:
                return render(request, 'polls/feedback.html', {'mssg': "enter the details"})

            print(ra, crop)
            print("rate", na['rate'])
            if feedback.objects.get(crop_name=crop) != "None":
                rr = feedback.objects.get(crop_name=crop)
                rz = int(rr.rate)
                ra = int((rz + ra) / 2)
                print(ra)
                rr.rate = ra
                rr.save()

            else:
                f = feedback(crop_name=crop, rate=ra)
                f.save()
            return render(request, 'polls/buyAndSell.html', {'name': nm})

    else:
        obj = corporate.objects.order_by().values('good_name').distinct()
        # print(obj)
        return render(request, 'polls/buyfarm.html', {'item': obj, 'name': nm})


### this function is for farmers to sell their prodcut via website
# they need to fill the details and based on authenticity of famer 
# it will be added to the data base 
def sell(request):
    if request.GET:
        # request.POST
        # form = sellerform(request.POST, request.FILES)
        # print("hello up ")
        # if form.is_valid():
        #    print("hello")
        #    form.save()
        na = request.GET
        # na=request.POST
        if "cancel" in na:
            return render(request, 'polls/seller.html')
        name = na['nam']
        ident = na['ident']
        crop = na['crop']
        price = na['price']
        max_kg = na['max']
        img = na['img']
        # img=na['img']["InMemoryUploadedFile"]
        if len(name) == 0 or len(ident) == 0 or max_kg == 0 or len(crop) == 0 or len(price) == 0:
            return render(request, 'polls/seller.html', {'mssg': "enter the details"})
        try:
            obj = verif.objects.get(user_name=name)
        except:
            return render(request, 'polls/seller.html', {'mssg': "invalid farmer id"})

        if obj.user_id == ident:
            # ,photo=img
            s = seller(user_name=name, crop_name=crop, price_per_kg=price, photo=img, max_kg=max_kg)
            s.save()
            all_obj = feedback.objects.all()
            feed = []
            for i in all_obj:
                a = feedback.objects.get(crop_name=i)
                # print(a.rate)
                feed.append(a)
            print(feed)
            return render(request, 'polls/buyAndSell.html', {'name': name, 'feed': feed})
        else:
            return render(request, 'polls/seller.html', {'mssg': "invalid farmer id"})
    else:
        return render(request, 'polls/seller.html')


# this for farmer to upload their crop picture
# adn to show for customers
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = sellerform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'polls/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = sellerform()
    return render(request, 'polls/upload.html', {'form': form})


# this is when a farmer forgots password they can cheange wth this functionality
# it is using phone number as a verifier  
def forgtpswrdfarm(request):
    if request.GET:
        na = request.GET
        if "cancel" in na:
            return render(request, 'polls/forgtpswrdfarm.html')
        name = na['who']
        pswrd = na['pass']
        phn = na['phn']
        repass = na['repass']
        if len(name) == 0 or len(pswrd) == 0 or len(phn) == 0 or len(repass) == 0:
            return render(request, 'polls/forgtpswrdfarm.html', {'mssg': "enter the details"})
        try:
            obj = farmer.objects.get(user_name=name)
        except:
            return render(request, 'polls/forgtpswrdfarm.html', {'mssg': "invalid user name"})

        if obj.phn == phn:
            if pswrd == repass:
                obj.password = pswrd
                obj.save()
                return HttpResponseRedirect('/polls/loginfarm/')
                # render(request,'polls/loginfarm.html',{'mssg':"password changed succesfully"})
            else:
                return render(request, 'polls/forgtpswrdfarm.html',
                              {'mssg': "re enter password should be same as new password"})

        else:
            return render(request, 'polls/forgtpswrdfarm.html', {'mssg': "phone number not matched"})
    else:
        return render(request, 'polls/forgtpswrdfarm.html')


# this is when a customer forgots password they can cheange wth this functionality
# it is using phone number as a verifier  

def forgtpswrd(request):
    if request.GET:
        na = request.GET
        if "cancel" in na:
            return render(request, 'polls/forgtpswrd.html')
        name = na['who']
        pswrd = na['pass']
        phn = na['phn']
        repass = na['repass']
        if len(name) == 0 or len(pswrd) == 0 or len(phn) == 0 or len(repass) == 0:
            return render(request, 'polls/forgtpswrd.html', {'mssg': "enter the details"})
        try:
            obj = table.objects.get(user_name=name)
        except:
            return render(request, 'polls/forgtpswrd.html', {'mssg': "invalid user name"})

        if obj.phn == phn:
            if pswrd == repass:
                obj.password = pswrd
                obj.save()
                return HttpResponseRedirect('/polls/login/')
                # render(request,'polls/login.html',{'mssg':"password changed succesfully"})
            else:
                return render(request, 'polls/forgtpswrd.html',
                              {'mssg': "re enter password should be same as new password"})

        else:
            return render(request, 'polls/forgtpswrd.html', {'mssg': "phone number not matched"})
    else:
        return render(request, 'polls/forgtpswrd.html')


## (rough)after farmer register add a verification page
##(rough) in verification page check with data base verif table


### (rough)right now i am at sign up page and nned to change signup page db connections something like that
## (rough)and need to do forgot passwrd page


## this for adding image to data bse and retrieving them
def gallery(request):
    obj = seller.objects.get(user_name="Harapriya Pal")
    # obj = seller.objects.get(user_name="Hari Samal")
    # obj = seller.objects.get(user_name="Jina Malik")
    # obj = seller.objects.get(user_name="Gourahari Pati")
    print(obj.photo.url)
    return render(request, 'polls/gallery.html', {"img": obj})
    # {"img":obj.photo}


###see the picture how to store and how to retrieve

# def showimage(request):
#    lastimage= seller.objects.last()
#    photo= lastimage.photo
#    form= ImageForm(request.POST or None, request.FILES or None)
#    if form.is_valid():
#        form.save()
#    context={'photo': photo,
#              'form': form
#            }
#    return render(request, 'polls/gallery.html', context)


# this is a redirecting function
def home(request):
    return render(request, 'polls/home.html')


def get_html_content(request):
    import requests
    city = request.GET.get('city')
    city = city.replace(" ", "+")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.google.com/search?q=weather+{city}').text
    return html_content


# this is for suggestions page
def sugg(request):
    result = None
    all_obj = feedback.objects.all()
    feed = []
    for i in all_obj:
        a = feedback.objects.get(crop_name=i)
        # print(a.rate)
        feed.append(a)
    print(feed)
    if request.GET:
        import requests
        na = request.GET
        city = na['city']
        html_content = get_html_content(request)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        result = dict()
        if soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}):
            # extract region
            result['region'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
            # extract temperature now
            result['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
            # get the day, hour and actual weather
            result['dayhour'], result['weather_now'] = soup.find("div",
                                                                 attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split(
                '\n')
        return render(request, 'polls/sugg.html', {'feed': feed, 'result': result})
    else:
        return render(request, 'polls/sugg.html', {'feed': feed})


# this is for contact us page
def contus(request):
    if request.GET:
        na = request.GET
        if len(na['nam']) == 0 or len(na['city']) == 0 or len(na['email']) == 0 or len(na['phn']) == 0 or len(
                na['query']) == 0:
            return render(request, 'polls/contactus.html', {'mssg': "enter the details"})

    return render(request, 'polls/contactus.html')


# this function displays all the customer items in the cart
def checkcart(request):
    print(nm)
    if nm == "None":
        print("hello")
    a = cart.objects.get(name=nm)
    items = []
    comp = []
    price = []
    s = a.seller_name.split(" ")
    img = []
    for se in s:
        img.append(seller.objects.get(user_name=se))

    print(img)
    pp = a.price.split(" ")
    suma = 0
    for el in pp:
        print(el + " ")
        suma += int(el)
        price.append(el)
    for k in s:
        print(k + " ")
        comp.append(k)
    kk = a.item.split(" ")

    for k in kk:
        print(k + " ")

        items.append(k)
    res = []
    if request.GET:
        email = []
        print(s)
        for k in s:
            sem = farmer.objects.get(user_name=k)
            email.append(sem.email)
        email_to = email
        if len(email) != 0:
            print(email_to)
            username = "project2wad@gmail.com"
            password = "Wad@project2#"
            smtp_server = "smtp.gmail.com:587"
            email_from = "project2wad@gmail.com"

            send_mail(
                "you got an order",
                "your order is for " + nm,
                email_from,
                email_to,
            )
            return render(request, 'polls/feedbackbuyer.html')
        else:
            return render(request, 'polls/choutcart.html',
                          {'name': nm, 'it': items, 'full': zip(comp, items, price, img), 'sum': suma, 'le': len(s)})
    else:
        # 'img':img,
        return render(request, 'polls/choutcart.html',
                      {'name': nm, 'it': items, 'full': zip(comp, items, price, img), 'sum': suma, 'le': len(s),
                       'media_url': settings.MEDIA_URL})
    # return render(request,'polls/choutcart.html',{'name':nm,'it':items,'full':zip(comp,items,price)})


# this function displays all the farmer items in the cart
def checkcartfarm(request):
    print(nm)
    if nm == "None":
        print("hello")
    a = cart.objects.get(name=nm)
    items = []
    comp = []
    price = []
    s = a.seller_name.split(" ")
    img = []
    for se in s:
        img.append(corporate.objects.get(company=se))

    print(img)

    pp = a.price.split(" ")
    suma = 0
    for el in pp:
        print(el + " ")
        suma += int(el)
        price.append(el)
    for k in s:
        print(k + " ")
        comp.append(k)
    kk = a.item.split(" ")

    for k in kk:
        print(k + " ")

        items.append(k)
    res = []
    if request.GET:
        email = []
        for k in s:
            sem = corporate.objects.get(company=k)
            email.append(sem.email)
        email_to = email
        if len(email) != 0:
            print(email_to)
            username = "project2wad@gmail.com"
            password = "Wad@project2#"
            smtp_server = "smtp.gmail.com:587"
            email_from = "project2wad@gmail.com"

            send_mail(
                "you got an order",
                "your order is for " + nm,
                email_from,
                email_to,
            )
            return render(request, 'polls/feedback.html')
        else:
            return render(request, 'polls/choutcart.html',
                          {'name': nm, 'it': items, 'full': zip(comp, items, price, img), 'sum': suma, 'le': len(s)})
    else:
        return render(request, 'polls/choutcart.html',
                      {'name': nm, 'it': items, 'full': zip(comp, items, price, img), 'sum': suma, 'le': len(s),
                       'media_url': settings.MEDIA_URL})


# this is to redirect to feedback page
def feed(request):
    return render(request, 'polls/feedback.html')

# (Rough)def hm(request):
# (Rough)    if request.GET:
# (Rough)       na=request.GET
# (Rough)       name=na['who']
# (Rough)        roll=na['roll']
# (Rough)        br=na['branch']
# (Rough)        cl=na['clg']
# (Rough)       s1=na['s1']
# (Rough)        s2=na['s2']
# (Rough)        s3=na['s3']
# (Rough)        s4=na['s4']
# (Rough)        s5=na['s5']
# (Rough)        t=int(s1)+int(s2)+int(s3)+int(s4)+int(s5)
# (Rough)        p=t/5
# (Rough)        return render(request,'polls/RESult.html',{"n":name,"r":roll,"br":br,"cl":cl,"s1":s1,"s2":s2,"s3":s3,"s4":s4,"s5":s5,"t":t,"p":p})
# (Rough)    else:
# (Rough)        return render(request,'polls/HOME1.html')
# (Rough)def index(request):
# (Rough)    return HttpResponse("hello world .you are at polls index .so in myproject .url server checks the maching in url patterns with --127.0.0.1:800/xxxx/ that xxx/ with any of the path in the urls pattern in path there are 4 argmnets we need only 2 or 3  one is route :like polls/ or xxx/ server checked with this ,next is view :when it find the match it creates an http request object and calls the view function and it returns a httpresponse and it may give some name for our purpose")
#
# (Rough)def results(request,question_id):
# (Rough)    text="you r looking at result of %s"
# (Rough)    return HttpResponse(text%question_id)
##(Rough) def index1(request):
# (Rough)    latest_q=Question.objects.order_by('-pub_date')[:5]
# (Rough)    output=', '.join([q.question_text for q in latest_q])
# (Rough)    return HttpResponse(output)


# (Rough)def index2(request):
# (Rough)    latest_question_list = Question.objects.order_by('-pub_date')[:5]#
# (Rough)    template = loader.get_template('polls/index.html')
# (Rough)    context = {
# (Rough)        'latest_question_list': latest_question_list,
# (Rough)   }
# (Rough)   return HttpResponse(template.render(context, request))


# (Rough)def index3(request):
# (Rough)    latest_question_list = Question.objects.order_by('-pub_date')[:5]
# (Rough)context = {
# (Rough)        'latest_question_list': latest_question_list,
# (Rough)    }
# (Rough)    return render(request,'polls/index1.html',context)

# (Rough)def detail(request, question_id):
# (Rough)    try:
# (Rough)        question = Question.objects.get(pk=question_id)
# (Rough)    except Question.DoesNotExist:
# (Rough)        raise Http404("Question does not exist")
# (Rough)    return render(request, 'polls/detail.html', {'question': question})
#
