from django.shortcuts import render,redirect
from authentication.models import User

# Create your views here.

def register(request):
    if request.method == "POST":
        
        user = User(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            phone_number = request.POST['phoneNo'],
            gender = request.POST['gender'],
            password = request.POST['pass1'],
        )
        
        user.save()
        return redirect('login')
        
    else:
        return render(request, 'register.html')