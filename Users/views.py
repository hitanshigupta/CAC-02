from django.shortcuts import render

def index(request):
    return render(request , 'Users/main/index.html')

# def DEF_NAME(request):
#     return render(request ,'Template path')
