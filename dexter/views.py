from genericpath import exists
from queue import Empty
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
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
            height_obtained = (float(datalist['height']) * 0.1)
            height_rounded = round(height_obtained, 2)

            weight_obtained = (float(datalist['weight']) * 0.1)
            weight_rounded = round(weight_obtained, 2)

            type1 = datalist['types'][0]['type']['name'].capitalize()
            type2=""
            try:
                if datalist['types'][1] in datalist['types']:
                    type2 = datalist['types'][1]['type']['name'].capitalize()
            except :
                type2 =""

            data = {
                "number": str(datalist['id']),
                "name": str(datalist['name']).capitalize(),
                "height": str(height_rounded),
                "weight": str(weight_rounded),
                "sprite": str(datalist['sprites']['front_default']),
                "type1": str(type1),
                "type2": str(type2),
            }

            print(data)
        else:
                data = {}
    except:
        messages.error(request, "No existe el Pokémon que has buscado 😢")
        return render(request, 'home.html')
    return render(request, 'home.html', data)