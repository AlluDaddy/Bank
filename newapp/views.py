from django.shortcuts import render, redirect
from django.contrib import messages
from newapp.models import Details

# Create your views here.



def main(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        mobile = request.POST["tel"]
        student_profile = Details.objects.create(name=name, email=email,password=password,mobile=mobile)
        student_profile.save()
        # user.set_password(user.password)#if custom is not working
        # user.save()
    # else:
        return render(request, 'greet.html',{"name":name,"mobile":mobile})

    #     return render(request, 'main.html',{"name":name,"email":email,"password":password,"mobile":mobile})
    return render(request, 'main.html')


