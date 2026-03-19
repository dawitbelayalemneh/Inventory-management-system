from django.shortcuts import render, redirect
from .models import Laptop, Desktop, Mobile
from .forms import LaptopForm, DesktopForm, MobileForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items': items,
        'header': 'Laptops'
    }
    return render(request, 'index.html', context)

def display_desktops(request):
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header': 'Desktops'
    }
    return render(request, 'index.html', context)

def display_mobiles(request):
    items = Mobile.objects.all()
    context = {
        'items': items,
        'header': 'Mobiles'
    }
    return render(request, 'index.html', context)

def add_laptop(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_laptops')
    else:
        form = LaptopForm()

    return render(request, 'add_new.html', {'form': form})

def add_desktop(request):
    if request.method == "POST":
        form = DesktopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_desktops')
    else:
        form = DesktopForm()

    return render(request, 'add_new.html', {'form': form})

def add_mobile(request):
    if request.method == "POST":
        form = MobileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_mobiles')
    else:
        form = MobileForm()

    return render(request, 'add_new.html', {'form': form})