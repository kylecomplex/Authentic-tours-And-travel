from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.views import generic

from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.


def home_view(request, *args, **kwargs):
    package = Package.objects.all().distinct().order_by('-id')[:4]
    context = {
        "package": package,
    }
    return render(request, "index.html", context)


def about_view(request, *args, **kwargs):
    return render(request, "about.html")


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html")


def services_view(request, *args, **kwargs):
    return render(request, "services.html")


def packages_view(request, *args, **kwargs):
    package = Package.objects.all().distinct().order_by('-id')
    context = {
        "package": package,
    }
    return render(request, "packages.html", context)


def booking_view(request, *args, **kwargs):
    return render(request, "booking.html")


def send_message(request):
    if request.method == "POST":
        name = request.POST.get('name').strip().capitalize()
        email = request.POST.get('email').strip()
        phone = request.POST.get('phone').strip()
        subject = request.POST.get('subject').strip()
        message = request.POST.get('message').strip()

        message_s = Message(name=name, email=email, phone=phone,
                            subject=subject, message=message)
        send_mail('Contact Form',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['calekorir@gmail.com'],
                  fail_silently=False)
        message_s.save()

        return redirect('contact')
    else:
        return redirect('contact')


def booking(request):
    if request.method == "POST":
        name = request.POST.get('name').strip().capitalize()
        email = request.POST.get('email').strip()
        phone = request.POST.get('phone').strip()
        date_created = request.POST.get('date_created').strip()
        adult = request.POST.get('adult').strip()
        kid = request.POST.get('kid').strip()
        message = request.POST.get('message').strip()

        booking = Booking(name=name, email=email, phone=phone, date_created=date_created, adult=adult, kids=kid, message=message)
        # send_mail('Contact Form',
        #           message,
        #           settings.EMAIL_HOST_USER,
        #           ['calekorir@gmail.com'],
        #           fail_silently=False)
        booking.save()

        return redirect('contact')
    else:
        return redirect('booking')
    
class ArticleList(generic.ListView):
    queryset = Post.objects.filter(poststatus=1).order_by('-created_on')
    template_name = 'article_list.html'


class ArticleDetail(generic.DetailView):
    model = Post
    template_name = 'article_detail.html'