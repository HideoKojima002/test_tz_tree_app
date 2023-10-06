from django.shortcuts import render
from .models import MenuItem


def workout(request):

    return render(request, 'index.html', {'name': 'name'})
