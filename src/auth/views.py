from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

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
        password = request.POST.get("password") or None

    return render(request, "auth/register.html", {})