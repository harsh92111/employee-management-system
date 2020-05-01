from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee    #reusability of employee model
        fields = ('fullname','emp_code','mobile','position') # '__all__' if we want all the fields of employee model
        labels = {'fullname':'Full Name',
                  'emp_code':'EMP. Code'}

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label='Select'