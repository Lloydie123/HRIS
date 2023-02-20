from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


from .forms import EmployeeForm,DepartmentForm
from .models import Employee,Department

# Create your views here.
class CreateEmployee(generic.CreateView):
    form_class = EmployeeForm
    template_name = "employee/employee_form.html"
    success_url = reverse_lazy("employee:index")
    context_object_name = "create_employee"


class UpdateEmployee(generic.UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employee/employee_form.html"
    success_url = reverse_lazy("employee:index")
    context_object_name = "update_employee"


class DeleteEmployee(generic.DeleteView):
    model = Employee
    success_url = reverse_lazy("employee:index")
    template_name = "employee/delete_form.html"
    context_object_name = "delete_employee"


class EmployeeListView(generic.ListView):
    model = Employee
    template_name = "employee/list_view.html"


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("employee:index")
    template_name = "employee/signup.html"

class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = "employee/detail_view.html"
    

# For Department

def dep(request):  
    if request.method == "POST":  
        form = DepartmentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_dep')  
            except:  
                pass  
    else:  
        form = DepartmentForm()  
    return render(request,'employee/department.html',{'form':form})  


def show_dep(request):  
    department = Department.objects.all()  
    return render(request,"employee/show_dep.html",{'department':department})  

def edit_dep(request, id):  
    department = Department.objects.get(id=id)  
    return render(request,'employee/edit_dep.html', {'department':department}) 

def update_dep(request, id):  
    department = Department.objects.get(id=id)  
    form = DepartmentForm(request.POST, instance = department)  
    if form.is_valid():  
        form.save()  
        return redirect("/employee/show_dep")  
    return render(request, 'employee/edit_dep.html', {'department': department})  

def destroy_dep(request, id):  
    department = Department.objects.get(id=id)  
    department.delete()  
    return redirect("/employee/show_dep")
