
# Create your views here.
from django.shortcuts import render,redirect
from .import forms




def category(request):
    if request.method =='POST':
       form =forms.Add_Category(request.POST)
       
       if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form =forms.Add_Category()
    return render(request,'add_category.html',{'form':form})