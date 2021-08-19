from django.shortcuts import render
from .models import Data

# Create your views here.
def home(request):
    return render(request=request, template_name='input_form/index.html', context={'data': Data.objects.all})