from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model, login

User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("signup")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("signup")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("signup")

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        login(request, user)
        messages.success(request, "Account created successfully!")
        return redirect("/")

    return render(request, "users/signup.html")




# from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm

# def signup(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'users/signup.html', {'form': form})

