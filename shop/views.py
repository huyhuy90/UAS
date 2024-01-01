from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from shop.forms import EmployeeForm  
from shop.models import Employee  

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())
def shop(request):
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())
def testimonial(request):
    template = loader.get_template('testimonial.html')
    return HttpResponse(template.render())
def why(request):
    template = loader.get_template('why.html')
    return HttpResponse(template.render())

def addnew(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = EmployeeForm()  
    return render(request,'siwil.html',{'form':form})  
 
def siwil(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
 
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
 
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'employee': employee})  
     
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/")  