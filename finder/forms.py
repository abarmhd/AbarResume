from socket import fromshare
from django import forms

atr = {'class':'form-control'}
class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs=atr))
    family = forms.CharField(widget=forms.TextInput(attrs=atr))
    email = forms.EmailField(widget=forms.EmailInput(attrs=atr))
    message = forms.CharField(widget=forms.Textarea(attrs=atr))

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 50:
            raise forms.ValidationError('The Name is Long.')
        elif len(name) < 3:
            raise forms.ValidationError('The Name is Small')
        return name
    
    def clean_family(self):
        family = self.cleaned_data['family']
        if len(family) > 50:
            raise forms.ValidationError('The Family is Long.')
        return family
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) > 1000:
            raise forms.ValidationError('The Message is Long.')
        return message