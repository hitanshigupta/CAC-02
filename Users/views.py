from django.shortcuts import render
from cadmin.models import Streets

def index(request):
    streets = Streets.objects.all()
    return render(request , 'Users/main/index.html', {'street': streets})

# def DEF_NAME(request):
#     return render(request ,'Template path')
