from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import AuthToken
# Create your views here.




@login_required
def home(request):
    current_user = request.user
    auth_user = AuthToken.objects.get(user=current_user)
    return render(request,'home/index.html',{'token' : str(auth_user.token)})


