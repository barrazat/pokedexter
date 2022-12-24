from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import  login

from django.contrib.auth.forms import  AuthenticationForm

from django.contrib.auth.models import  User

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
import json, urllib
# Create your views here.
def home(request):
    try:
        if request.method == 'POST':
            pokemon = request.POST['pokemon'.lower()]
            pokemon = pokemon.replace(' ', '%20')
            url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
            url_pokeapi.add_header('User-Agent', 'charmander')

            source = urllib.request.urlopen(url_pokeapi).read()
            datalist = json.loads(source)
            data = {
                "number": str(datalist['id']),
                "name": str(datalist['name']).capitalize(),
                "height": str(datalist['height']*0.1),
                "weight": str(datalist['weight']*0.1),
                "sprite": str(datalist['sprites']['front_default']),
                "type1": str(datalist['types'][0]['type']['name']).capitalize(),
                "type2": str(datalist['types'][1]['type']['name']).capitalize(),
            }

            print(data)
        else:
                data = {}
    except:
        raise Http404("no esta")
    return render(request, 'home.html', data)