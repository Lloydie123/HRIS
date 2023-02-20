from django import forms
from .models import Employee,Department
from django.forms import fields

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields  = '__all__'
        widgets = {
            'dateBirth': forms.DateInput(attrs={'type': 'date'}),
             'gender': forms.RadioSelect,
        }

class DepartmentForm(forms.ModelForm):  
    class Meta:  
        model = Department  
        fields = ('name','description')