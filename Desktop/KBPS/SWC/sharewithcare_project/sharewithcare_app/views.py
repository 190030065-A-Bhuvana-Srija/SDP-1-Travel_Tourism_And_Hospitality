import pandas as pd
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from pulp import *
import pytest

from .forms import *
from .models import KulfisModel, DairyModel, CakesModel, BeveragesModel, SweetsModel, CreamModel, BestSellers


def index(request):
    return render(request, 'homepage.html')


def logout(request):
    return HttpResponse('User Logged Out Successfully!')


def rawproducts(request):
    data = Add.objects.all()
    return render(request, 'rawproducts.html', {'data': data})


def listofinterproducts(request):
    data = List.objects.all()
    return render(request, 'listofinterproducts.html', {'data': data})


def Sweets(request):
    data = SweetsModel.objects.all()
    return render(request, 'sweets.html', {'data': data})


def Beverages(request):
    data = BeveragesModel.objects.all()
    return render(request, 'beverages.html', {'data': data})


def Cakes(request):
    data = CakesModel.objects.all()
    return render(request, 'cakes.html', {'data': data})


def Dairy(request):
    data = DairyModel.objects.all()
    return render(request, 'dairy.html', {'data': data})


def Kulfis(request):
    data = KulfisModel.objects.all()
    return render(request, 'kulfis.html', {'data': data})


def curd(request):
    data = CurdModel.objects.all().values()
    curd_df = pd.DataFrame(data)
    curd_stock = curd_df['quantity']
    data2 = CurdModel.objects.all()
    subject = 'Share With Care (SWC)'
    message = f'Greetings! Curd Stock Exists.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['prakashsharmayv@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return render(request, 'curdbrands.html', {'data' : data2, 'curd_stock' : curd_stock})


def ghee(request):
    data = GheeModel.objects.all().values()
    curd_df = pd.DataFrame(data)
    curd_stock = curd_df['quantity']
    data2 = GheeModel.objects.all()
    subject = 'Share With Care (SWC)'
    message = f'Greetings! Ghee Stock Exists.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['prakashsharmayv@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return render(request, 'gheebrands.html', {'data' : data2})


def paneer(request, toAddress='prakashsharmayv@gmail.com'):
    data = PaneerModel.objects.all().values()
    curd_df = pd.DataFrame(data)
    curd_stock = curd_df['quantity']
    data2 = PaneerModel.objects.all()
    subject = 'Share With Care (SWC)'
    message = f'Greetings! Paneer Stock Exists.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['prakashsharmayv@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return render(request, 'paneerbrands.html', {'data': data2})


def cream(request, toAddress='prakashsharmayv@gmail.com'):
    data = CreamModel.objects.all().values()
    curd_df = pd.DataFrame(data)
    curd_stock = curd_df['quantity']
    data2 = CreamModel.objects.all()
    subject = 'Share With Care (SWC)'
    message = f'Greetings! Cream Stock Exists..'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['prakashsharmayv@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return render(request, 'creambrands.html', {'data': data2})


def butter(request, toAddress='prakashsharmayv@gmail.com'):
    data = ButterModel.objects.all().values()
    curd_df = pd.DataFrame(data)
    curd_stock = curd_df['quantity']
    data2 = ButterModel.objects.all()
    subject = 'Share With Care (SWC)'
    message = f'Greetings! Butter Stock Exists.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['prakashsharmayv@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return render(request, 'butterbrands.html', {'data': data2})


def interproducts(request):
    data = Add2.objects.all()
    return render(request, 'interproducts.html', {'data': data})


def endproducts(request):
    data = Add3.objects.all()
    messages.success(request, 'Added To Cart Successfully!')
    return render(request, 'endproducts.html', {'data': data})


def addrawproducts(request):
    form = AddForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addrawproducts.html')
    return render(request, 'addrawproducts.html', {'form': form, 'data': Add.objects.all()})


def addinterproducts(request):
    form = Add2Form(request.POST, request.FILES)
    if request.method == 'POST':
        form = Add2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addinterproducts.html')
    img_obj = form.instance
    return render(request, 'addinterproducts.html', {'form': form, 'data': 'Add2.objects.all()', 'img_obj': img_obj})


def addendproducts(request):
    form = Add3Form(request.POST, request.FILES)
    if request.method == 'POST':
        form = Add3Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addendproducts.html')
    img_obj = form.instance
    return render(request, 'addendproducts.html', {'form': form, 'data': 'Add3.objects.all()', 'img_obj': img_obj})


def cart(request):
    return render(request, 'cart.html')


def pay(request):
    username = request.POST.get("username", "absrija16")
    subject = 'Share With Care (SWC)'
    message = f'Greetings {username}! Your order has been placed successfully! You will be notified as soon as the order starts boarding.\nUntil then, Enjoy Shopping!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["bhuvanasrija1692@gmail.com"]
    html_content = render_to_string("ordertrack.html", {'content' : message})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        subject,
        text_content,
        email_from,
        recipient_list
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

    return render(request, 'pay.html')


def bestsellers(request):
    data = BestSellers.objects.all()
    return render(request, 'bestsellers.html', {'data': data})


def luck(request):
    return render(request, 'luck.html')


def email(request):
    return render(request, 'email.html')

from .models import CurdModel, ButterModel, GheeModel, PaneerModel


def cart(request):
    data = ButterModel.objects.all().values()
    data2 = ButterModel.objects.all()
    mydf = pd.DataFrame(data)
    sum = mydf['price'].sum()
    le = mydf['name'].count()
    if le != 0 :
        stock = True
    model = LpProblem('Minimize The Total Cost', sense=LpMaximize)
    C = LpVariable('C', lowBound=0, upBound=None, cat='Integer')
    P = LpVariable('P', lowBound=0, upBound=None, cat='Integer')
    model += 45 * C + 30 * P
    model += 1 * C + 0.5 * P <= 15
    model += 1 * C + 1 * P <= 10
    model += 0.5 * C + 1 * P <= 70
    status2 = LpStatus[model.status]
    model.solve()
    before = sum
    after = sum - C.varValue + P.varValue
    status = LpStatus[model.status]
    return render(request, 'cartpage.html', {'full' : data,'status2' : status2, 'data2' : data2, 'sum' : sum, 'le' : le, 'stock' : stock, 'status' : status, 'before' : before, 'after' : after})

def ordertrack(request):
    data = ButterModel.objects.all().values()
    data2 = ButterModel.objects.all()
    mydf = pd.DataFrame(data)
    sum = 57
    le = mydf['name'].count()
    if le != 0:
        stock = True
    withtax = 15
    withdeliv = 10
    tot = sum + withtax + withdeliv
    return render(request, 'ordertrack.html', {'full': data,'tot' : tot, 'data2': data2, 'sum': sum, 'le': le, 'stock': stock, 'withtax' : withtax, 'withdeliv' : withdeliv})

def progress(request):
    return render(request, 'progress_bar.html')