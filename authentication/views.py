from django.shortcuts import render, redirect
from authentication.models import User, Category,Contact
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


def register(request):
    if request.method == "POST":

        # Hash the password before saving the user
        hashed_password = make_password(request.POST["pass1"])

        user = User(
            first_name=request.POST["fname"],
            last_name=request.POST["lname"],
            email=request.POST["email"],
            phone_number=request.POST["phoneNo"],
            gender=request.POST["gender"],
            password=hashed_password,
        )

        user.save()
        return redirect("login")

    else:
        return render(request, "register.html")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                # Start session
                request.session["user_id"] = user.id
                request.session["user_email"] = user.email
                request.session["user_name"] = f"{user.first_name} {user.last_name}"
                request.session.set_expiry(3600)  # Session expiry in seconds
                return redirect("memberspage")  # Redirect to members page
            else:
                messages.error(request, "Invalid email or password.")
                return redirect("login")
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect("login")
    else:
        return render(request, "login.html")


def logout(request):
    # Clear session data
    try:
        del request.session["user_id"]
        del request.session["user_name"]
        del request.session["user_email"]
    except KeyError:
        pass  # In case the session data does not exist

    # Redirect to login page or home page
    return redirect("login")  # or replace with another URL if needed

def membersPage(request):
    # Check if the user is logged in
    if "user_id" not in request.session:
        return redirect("login")  # Redirect to login page if not logged in

    # Retrieve session data
    user_id = request.session.get("user_id")
    
    try:
        # Fetch the user data from the database
        user = User.objects.get(id=user_id)
        
        if request.method == "POST":
            # Handle form submission
            first_name = request.POST.get("fname")
            last_name = request.POST.get("lname")
            email = request.POST.get("email")
            phone = request.POST.get("phoneNo")
            gender = request.POST.get("gender")

            # Update user details
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.phone_number = phone
            user.gender = gender
            user.save()

            # Feedback message
            messages.success(request, "Profile updated successfully!")

            return redirect("memberspage")  # Reload the page to reflect changes

        # Pass the user data to the template for rendering
        context = {
            "user_id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "user_email": user.email,
            "user_phone": user.phone_number,
            "user_gender": user.gender,
        }
        return render(request, "memberspage.html", context)
    except User.DoesNotExist:
        # Handle the case where the user doesn't exist in the database
        messages.error(request, "User not found")
        return redirect("login")



def pricing(request):

    courses = Category.objects.all()
    return render(request, "pricing.html", {"courses": courses})

def contact(request):
    user_id = request.session.get("user_id")
    context = {}

    if user_id:
        try:
            user = User.objects.get(id=user_id)
            context = {
                "fname": user.first_name,
                "lname": user.last_name,
                "email": user.email,
                "phone": user.phone_number,
            }
        except User.DoesNotExist:
            pass

    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')

        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            query=query
        )
        contact.save()
        messages.success(request, "Message sent successfully!")
        return redirect('contact')

    return render(request, "contact.html", context)



def delete_account(request):
    if request.method == "POST":  # Ensure the method is POST
        user_id = request.session.get("user_id")
        
        try:
            user = User.objects.get(id=user_id)
            user.delete()  # Delete the user from the database
            
            # Clear session data after deletion
            request.session.flush()
            
            messages.success(request, "Your account has been deleted successfully.")
            return redirect("login")  # Redirect to the register page or another appropriate page
        except User.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect("register")
    else:
        # If the method is not POST, redirect to the members page
        messages.info(request, "Invalid request method.")
        return redirect("memberspage")

