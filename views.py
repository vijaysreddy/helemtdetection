from django.shortcuts import render
from django.http import HttpResponse
from .models import Images
from .forms import *
from django.views.decorators.csrf import csrf_exempt
import os
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def image_upload(request): 
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save()
            image_path = os.getcwd()+'/media/images/'+form.cleaned_data['imageId']
            # saved =  detect_faces(image_path) 
            return redirect('success') 
    else: 
        form = ImageForm() 
    return render(request, 'image_collector/class_image_form.html', {'form' : form}) 


def view_images(request):
    context = {
        # 'images' : Images.objects.filter(imageId="test").first()
        'images' : Images.objects.all()
    }
    return render(request, 'image_collector/view_images.html', context)