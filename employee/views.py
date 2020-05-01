from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee_list(request):
    context = {'employee_list' : Employee.objects.all()}  #to show the list on the html page and then make a table in html page
    return render(request, 'employee_list.html',context)

def employee_form(request, id=0):#as form action is empty form submission will happen in same page...so we will use get and post method
    if request.method == "GET":
        if id==0:                          #id is 0 during insert and !0 during update
            form=EmployeeForm()
        else:
            employee=Employee.objects.get(pk=id)  #this will get the corresponding id record and from the form u can edit it and post it
            form=EmployeeForm(instance=employee)
        return render(request,"employee_form.html",{'form':form})
    else:
        if id==0:
            form=EmployeeForm(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request, id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

