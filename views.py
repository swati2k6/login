from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user_profile")  # go create profile
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

@login_required
def dashboard_redirect(request):
    try:
        profile = request.user.profile
        if profile.user_type == "doctor":
            return redirect("/dashboard/doctor")
        elif profile.user_type == "patient":
            return redirect("/dashboard/patient")
    except UserProfile.DoesNotExist:
        return redirect("user_profile")  # force profile setup
    return redirect("login")