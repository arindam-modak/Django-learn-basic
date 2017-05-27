from django.shortcuts import render

email = 'arindam.modak03@gmail.com'

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me',email]})

