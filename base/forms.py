from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import  UserChangeForm, SetPasswordForm
from .models import Profile

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.TextInput(attrs={'type': 'password'}))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este endereço de email já está em uso.")
        return email

from .models import Profile


class UserInfoForm(forms.ModelForm):
	celular = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'celular'}), required=False)
	endereço = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'endereço'}), required=False)
	cidade = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'cidade'}), required=False)
	estado = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'estado'}), required=False)


	class Meta:
		model = Profile
		fields = ('celular', 'endereço',  'cidade', 'estado' )



class ChangePasswordForm(SetPasswordForm):
	class Meta:
		model = User
		fields = ['new_password1', 'new_password2']

	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Senha'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = ''

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Senha'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Senha antiga.</small></span>'

class UpdateUserForm(UserChangeForm):
	# Hide Password stuff
	password = None
	# Get other fields
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email '}), required=False)
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}), required=False)

	class Meta:
		model = User
		fields = ('username', 'first_name',  'email')

	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'usuario'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
