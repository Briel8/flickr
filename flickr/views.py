import os
from pathlib import Path
import environ
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserIdForm

import requests

# initial setup
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR, '.env')

def index(request):
    """
    Renders the index page with the form.
    """

    if request.method == 'POST':
        user_id = request.POST['user_id']
        return redirect('flickr:search', user_id=user_id)
    form = UserIdForm()
    return render(request, 'flickr/index.html', {'form': form})

def search(request, user_id):
    method = '?method=flickr.photos.search'
    api_key = f'&api_key={env('KEY')}'
    pk = f'&user_id={user_id}'
    form = '&format=json&nojsoncallback=1'
    url = f'https://www.flickr.com/services/rest/{method}{api_key}{pk}{form}'

    response = []
    try:
        response = requests.get(url).json()
    except:
        return HttpResponse("Hello! You're seing me probably because 'SOMETHING WHENT WRONG'")
    
    photo_urls = []
    data = response['photos']['photo']
    for photo_data in data:
        photo_urls.append(f'https://live.staticflickr.com/{photo_data['server']}/{photo_data['id']}_{photo_data['secret']}_w.jpg')
    return render(request, 'flickr/results.html', {'photos': photo_urls})