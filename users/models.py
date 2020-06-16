from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import uuid
# Create your models here.



class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class AuthToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4)


