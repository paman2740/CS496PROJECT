from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.db import transaction
from .models import User,Witness,Officer, Case, LineUp, finalPhoto

class WitnessSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)
    case = forms.ModelMultipleChoiceField(required=False,queryset=Case.objects.all())


    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_witness = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        witness = Witness.objects.create(user=user)
        witness.phone_number=self.cleaned_data.get('phone_number')
        witness.location=self.cleaned_data.get('location')
        witness.case.set(self.cleaned_data.get('case'))
        witness.save()
        return user

class OfficerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_officer = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        officer = Employee.objects.create(user=user)
        officer.phone_number=self.cleaned_data.get('phone_number')
        officer.designation=self.cleaned_data.get('designation')
        officer.save()
        return user

class LineUpForm(ModelForm):
    class Meta:
        model = LineUp
        fields = ('user', 'case')
        labels = {
            'user': 'User',
            'case': 'Case',
            #'photo': 'Photo',          
        }
        widgets = {
            'user': forms.Select(attrs={'class':'form-control', 'placeholder':'User'}),
            'case': forms.Select(attrs={'class':'form-control', 'placeholder':'Case'}),
            #'photo': forms.Select(attrs={'class':'form-control', 'placeholder':'Photo'}),
            
        }