from django.shortcuts import render
from .forms import ImageUploadForm
from .preprocessing import Hough_Transform, OCR

import numpy as np

# Create your views here.
def handle_uploaded_file(f):
    with open('img.png','wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def home(request):
    return render(request,'index.html')


def imageprocess(request):
    form =ImageUploadForm(request.POST,request.FILES)
    if form.is_valid():

        handle_uploaded_file(request.FILES['image'])
        img_path='img.png'
        Hough_Transform(img_path)
        res = OCR()
        return render(request,'output.html',{'res':res})
    return render(request,'index.html')
