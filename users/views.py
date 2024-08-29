from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    form = UserCreationForm() # Creates an instance of the form.
    return render(request, 'users/register.html', {'form': form})