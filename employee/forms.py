from django import forms


from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields  = '__all__'
        widgets = {
            'dateBirth': forms.DateInput(attrs={'type': 'date'}),
             'gender': forms.RadioSelect,
        }

