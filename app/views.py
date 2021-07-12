from django.shortcuts import render
from django.views.generic import ListView
from .models import Slider,Marketing, Feature


# Create your views here.
# class HomePageView(ListView):
#     model = Slider
#     template_name = 'index.html'


def HomePageView(request):
    feature = Feature.objects.all()
    marketing = Marketing.objects.all()
    slider = Slider.objects.all()
    context = {"slider": slider, "feature": feature, "marketing":marketing}
    return render(request, 'index.html', context)
