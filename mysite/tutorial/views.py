from django.shortcuts import render
from .models import Person
from django_tables2 import RequestConfig
from .tables import PersonTable

# Create your views here.
def people(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    return render(request,'people.html',{'table':table})
