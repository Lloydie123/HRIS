from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


from .forms import EmployeeForm
from .models import Employee

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


class ListView(generic.ListView):
    model = Employee
    template_name = "employee/list_view.html"


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("employee:index")
    template_name = "employee/signup.html"
