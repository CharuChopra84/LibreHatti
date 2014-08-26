from django.forms import ModelForm, TextInput
from models import SuspenseClearance
from models import TaDa
from models import SuspenseOrder
from models import Staff
from django import forms

# Create your forms here.
class Clearance_form(ModelForm):
    class Meta:
        model = SuspenseClearance
        fields = ['work_charge','labour_charge','car_taxi_charge',
                  'boring_charge_external','boring_charge_internal',
		  'lab_testing_staff','field_testing_staff','test_date']


class SuspenseForm(ModelForm):
    class Meta:
        model = SuspenseOrder
        exclude = ('is_cleared',)
      
class TaDaSearch(forms.Form):
    ref_no = forms.ModelChoiceField(queryset= SuspenseOrder.objects.all())

class TaDaForm(ModelForm):
    class Meta:
        model = TaDa
        exclude = ('',)

class Programme_letter(forms.Form):
    Address = forms.CharField(max_length=50)
    ClientContact = forms.CharField(max_length= 500)
    Subject = forms.CharField(max_length=500)
    Site_Venue = forms.CharField(max_length=500)
    Site_Date = forms.DateField()
    Site_Time = forms.TimeField()
    Staff = forms.ModelMultipleChoiceField(queryset=Staff.objects.all(), widget=forms.CheckboxSelectMultiple())


