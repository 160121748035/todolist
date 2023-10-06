from django.shortcuts import render,HttpResponse
from todoapp.models import task
# Create your views here.
def home(request):
    context={'success':False}
    if request.method=="POST":
        task1=request.POST['task']
        taskdesc1=request.POST['info']
        ins=task(taskname=task1,taskdesc=taskdesc1)
        ins.save()
        context['success']=True
    return render(request,'index.html',context)
def tasks(request):
    alltasks=task.objects.all()
    context={'tasks':alltasks}
    return render(request,'about.html',context)
def delete(request):
    param1 = request.GET.get('param1')
    data=task.objects.all()
    context={'tasks':data}
    for i in data:
        if i.taskname==param1:
            i.delete()
            break
    # data.delete()
    return render(request,'about.html',context)
    
    