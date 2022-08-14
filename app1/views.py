from django.shortcuts import render
from .forms import imgModelForm
from .models import imgModel
# Create your views here.
def home(request):
    if request.method=='POST':
        form=imgModelForm(request.POST,request.FILES) #iss line our home.html mei line 16 ka khas khyal rkhna hia
        if form.is_valid():                            #wrna kaam nhi krayga.
            form.save()
    form=imgModelForm()
    img=imgModel.objects.all()
    return render(request,'app1/home.html',{'form':form,'img':img})