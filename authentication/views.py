from django.shortcuts import render, redirect
from authentication.models import User, Category
from django.contrib.auth.hashers import make_password, check_password
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




def membersPage(request):
    # Check if the user is logged in
    if "user_id" not in request.session:
        return redirect("login")  # Redirect to the login page if not logged in

    # Retrieve session data
    user_id = request.session.get("user_id")

    # Fetch the user data from the database
    user = User.objects.get(id=user_id)

    # Pass the user data to the template
    context = {
        "user_id": user.id,
        "user_name": f"{user.first_name} {user.last_name}",
        "user_email": user.email,
        "user_phone": user.phone_number,
        "user_gender": user.gender,
    }
    return render(request, "memberspage.html", context)




def pricing(request):

    courses = Category.objects.all()
    return render(request, "pricing.html", {"courses": courses})
