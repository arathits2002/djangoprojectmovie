from django.shortcuts import render
from movieapp.forms import addform
from movieapp.models import addmodel

# Create your views here.

def home(request):
    m=addmodel.objects.all()
    return render(request,'home.html',{'view':m})

def Addmovie(request):
    form=addform()
    if(request.method=="POST"):
        form=addform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'Addmovie.html',{'form':form})
def viewdetails(request,p):
    v=addmodel.objects.get(id=p)
    return render(request,'viewdetails.html',{'details':v})


def updatemovie(request,p):
    u=addmodel.objects.get(title=p)
    form=addform(instance=u)
    if(request.method=="POST"):
        form = addform(request.POST,request.FILES,instance=u)
        if(form.is_valid()):
            form.save()
        return home(request)

    return render(request,'Addmovie.html',{'form':form})

def deletemovie(request,p):
    m=addmodel.objects.get(title=p)
    m.delete()
    return home(request)
