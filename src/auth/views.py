from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == "POST":
        username = request.POST.get("username") or None
        password = request.POST.get("password") or None

        if all([username, password]):
            user = authenticate(request, username=username, password=password)

            if user is not None:
                print("User authenticated")
                login(request, user)
                return redirect("/")

            print(f"User is authenticated: {request.user.is_authenticated}")

    return render(request, "auth/login.html", {})

def register_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == "POST":
        username = request.POST.get("username") or None
        email = request.POST.get("email") or None
        password = request.POST.get("password") or None
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect("/")
        except Exception as e:
            pass

    return render(request, "auth/register.html", {})