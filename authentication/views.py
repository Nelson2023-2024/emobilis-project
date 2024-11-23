from django.shortcuts import render,redirect
from authentication.models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def register(request):
    if request.method == "POST":
        
         # Hash the password before saving the user
        hashed_password = make_password(request.POST['pass1'])
        
        user = User(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            phone_number = request.POST['phoneNo'],
            gender = request.POST['gender'],
            password = hashed_password
        )
        
        user.save()
        return redirect('login')
        
    else:
        return render(request, 'register.html')
    
    
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email)
            
            if check_password(password, user.password):
                return redirect('memberspage')
            else:
                return render(request, 'login.html')
        except User.DoesNotExist:
            # # User not found
            # messages.error(request, "Invalid email or password.")
            return render(request, 'login.html')
        
    else:
        return render(request, 'login.html')

def membersPage(request):
    return render(request, "memberspage.html")