from django.shortcuts import render
from exhibition.models import Exhibition
from festival.models import Festival

def home(request):
    exhibitions = Exhibition.objects.all().order_by('-pk')[:2]
    festivals = Festival.objects.all().order_by('-pk')[:2]
    return render(request, "index.html", {'exhibitions': exhibitions, 'festivals': festivals})
# Create your views here.
