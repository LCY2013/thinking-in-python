from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello Django!")


# path('<int:year>', views.year),
def year(request, year):
    # return HttpResponse(year)
    return redirect('/2023.html')


# path('<int:year>/<str:name>', views.name),
def name(request, **kwargs):
    return HttpResponse(kwargs['name'])


# path('<myint:year>', views.year),
# re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
def myyear(request, year):
    print(year)
    return render(request, 'yearview.html')
