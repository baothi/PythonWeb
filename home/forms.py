from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesnotExist

class RegistrationForm(forms.Form):
	username = forms.CharField(lable='Tài Khoản', max_length=30)
	email = forms.EmailField(lable='Email')
	password1 = forms.CharField(lable='Mật Khẩu', widget=forms.passwordInput())
	password2 = forms.CharField(lable='Nhập Lại Mật Khẩu', widget=forms.passwordInput)

	def clean_password2(self):
		if 'password1' in self.leaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
			if password1==password2 and password1:
				return password2
		raise forms.validationError("Mật Khẩu không Hợp Lệ")
	def clean_username(self):
		username = self.cleaned_data['username']
		if re.search(r'^\w+$', username):
			raise forms.validationError("ten tai khoan co ky tu dac biet")
		try:
			User.objects.get(username=username)

		except ObjectDoesnotExist:
			return username
		raise forms.validationError("tai khoan da ton tai")
	def save(self):
		User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])