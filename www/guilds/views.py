from django.shortcuts import render
from django.http import Http404
from .models import Guild


# Create your views here.


def index(request):
    context = {}
    try:
        guilds = Guild.objects.all()
        context.update({"guilds": guilds})
    except Exception:
        raise Http404("Can't render 'guilds/' view")
    return render(request, 'guilds/index.html', context)