from django import forms
class ContactForm(forms.Form):
	name = forms.CharField(required=True)
	from_email = forms.EmailField(required=True)
	mobile_no = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
	messages = forms.CharField(widget=forms.Textarea, required=True)