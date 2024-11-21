from audioop import reverse

from django.shortcuts import render, redirect

from user.models import User


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            user = User.objects.create_user(username, email, password)
            if user:
                login(request, user)
            return redirect(reverse("user:details"))
    else:
        return render(request, 'user/register.html')