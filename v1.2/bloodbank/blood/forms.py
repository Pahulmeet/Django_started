from django.contrib.auth.models import User
from django import forms
from .models import Blood_request


'''
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    city = forms.CharField(max_length=100)
    blood_group = forms.CharField(max_length=3)
    state = forms.CharField(max_length=100)
    contact1 = forms.IntegerField()
    contact2 = forms.IntegerField()
    pin_code = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'city', 'pin_code', 'state', 'contact1', 'contact2', 'blood_group']
'''
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']




#HOSPITAL SIGN UP
class HospitalForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'City'
        }
    ))
    pin_code = forms.CharField(max_length=7, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Pin Code'
        }
    ))
    state = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'State'
        }
    ))
    contact1 = forms.CharField(max_length=13, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contact1'
        }
    ))
    contact2 = forms.CharField(max_length=13, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contact2'
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'city', 'pin_code', 'state', 'contact1', 'contact2']





#DONOR SIGN UP
class DonorForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'City'
        }
    ))
    pin_code = forms.CharField(max_length=7, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Pin Code'
        }
    ))
    state = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'State'
        }
    ))
    contact1 = forms.CharField(max_length=13, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contact1'
        }
    ))
    contact2 = forms.CharField(max_length=13, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contact2'
        }
    ))
    blood_group = forms.CharField(max_length=3, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'A+/B+/AB+/O+/A-/B-/AB-/O-'
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'city', 'pin_code', 'state', 'contact1', 'contact2', 'blood_group']


'''
    def save(self, commit=True):
        user = super(HospitalForm, self).save(commit=False)
        user.username = self.cleaned_data('username')
        user.city = self.cleaned_data('city')
        user.pin_code = self.cleaned_data('pin_code')
        user.contact1 = self.cleaned_data('contact1')
        user.contact2 = self.cleaned_data('contcat2')
        user.email = self.cleaned_data('email')
        user.state = self.cleaned_data('state')

        if commit:
            user.save()

            return user
'''


# REQUEST BLOOD
class RequestForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name'
        }
    ))

    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'City'
        }
    ))

    pin_code = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Pin Code'
        }
    ))

    contact1 = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contact1'
        }
    ))

    contact2 = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contact2'
        }
    ))

    date = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'YYYY-MM-DD'
        }
    ))

    blood_group = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'A+/B+/AB+/O+/A+/B-/AB-/O-'
        }
    ))


    class Meta:
        model = Blood_request
        fields = ['name', 'city', 'pin_code', 'contact1', 'contact2', 'date', 'blood_group']



#LOGIN
class Login(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }
    ))
    class Meta:
        model = User
        fields = ['username','password']