from django.shortcuts import render
from .forms import ProductForm, Video_form
from .models import Product, Video, Room
from django.shortcuts import render, HttpResponse, redirect



# Create your views here.





def games(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "accounts/games.html", context)


def upload(request):
    form = ProductForm()
    if request.method == "POST":
        print(request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "accounts/upload.html", context)


def index(request):

 all_video = Video.objects.all()
 #if request.method == "POST":
   # form = Video_form(data=request.POST, files=request.FILES)
    #if form.is_valid():
       # form.save()
        #return HttpResponse("<h1> Uploaded successfully </h1>")
 #else:
 form = Video_form()
 return render(request, 'accounts/coach-page.html', {"form": form, "all": all_video})


def all_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'accounts/index.html', {'rooms': rooms})


def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, 'accounts/room_detail.html', {'room': room})


def videos(request):

 all_video = Video.objects.all()
 form = Video_form()
 return render(request, 'accounts/subscription-page.html', {"form": form, "all": all_video})


def profile (request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "accounts/profile.html", context)