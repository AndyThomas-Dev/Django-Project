from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from users.forms import CustomUserCreationForm


def dashboard(request):
    return render(request, "users/dashboard.html")


def register(request):
    # gets users/register.html
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
