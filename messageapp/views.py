from django.shortcuts import render,HttpResponse,redirect
from messageapp.models import Msg


# Create your views here.
def create(request):
    # print("Request is:",request.method)
    if request.method=="GET":
        # print("in if section")
        return render(request,'create.html')
    else:
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        # create objects as 
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg,)

        m.save()
        return redirect('/dashboard')
   
        # -----------------------
        # print("Name:",n)
        # print("mail:",mail)
        # print("mobile:",mob)
        # print("messages",msg)
        # return HttpResponse("insert data into database")
    
def dashboard(request):
    m=Msg.objects.all()
    print(m)
    context={}
    context["data"]=m
    return render(request,'dashboard.html',context)

def delete(request,rid):
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')
    

def edit(request,rid):
    if request.method=="GET":   
        m=Msg.objects.filter(id=rid)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    else:
        upname=request.POST['uname']
        upmail=request.POST['uemail']
        upmob=request.POST['mobile']
        upmsg=request.POST['msg']
        # create objects as
        m=Msg.objects.filter(id=rid)
        m.update(name=upname,email=upmail,mobile=upmob,msg=upmsg)
        return redirect('/dashboard')
    









































