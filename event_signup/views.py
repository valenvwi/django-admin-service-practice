from django.shortcuts import render
from .forms import SignupForm
from .models import Form
from django.contrib import messages

def index(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]

            Form.objects.create(first_name=first_name, last_name=last_name, email=email)

            print("Signup submitted successfully")


            messages.add_message(request, messages.SUCCESS, "Signup successfully!")

    return render(request, "index.html")
