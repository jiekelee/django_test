from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date
from .models import fileModel
from .tables import fileTable
from django_tables2 import RequestConfig

def index(request):
    # return HttpResponse("welcome")
    today = str(date.today())
    word = "hello,today is " + today
    table = fileTable(fileModel.objects.all())
    RequestConfig(request).configure(table)
    return render(request,'index.html',{'baoshi':word,'biaoge':table})

def result_cloud(request):
    if request.method == 'POST':
        data = request.FILES['myfile']
        file = fileModel(myfile=data)
        file.save()
        return redirect('/')
    else:
        return HttpResponse("Sorry the upload is faild.")

def listall(request):
    all_data = fileModel.objects.all()
    file_table = ""
    for file in all_data:
        file_table += '%s' % (file.myfile)
    return render(request,'list.html',{'alllist':file_table})
    pass

def delete_view(request,file_id):
    try:
        u = fileModel.objects.get(id=file_id)
        u.delete()
    except:
        pass
    return redirect('/')































