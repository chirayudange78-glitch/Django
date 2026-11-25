from django.shortcuts import render
from .models import *
# Create your views here.
def receipes(request):
    if request.method == "POST":

        data = request.POST
        recepie_image = request.FILES.get('recepie_image')
        recepie_name =  data.get('recepie_name')
        recepie_descripiton = data.get('recepie_descripiton')
   
    
        recepie.objects.create(
            recepie_image = recepie_image,
            recepie_name  = recepie_name,
            recepie_descripiton = recepie_descripiton,


         )


    return render(request , 'receipes.html')
