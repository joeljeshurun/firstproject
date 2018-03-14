from django import forms
from django.forms.widgets import HiddenInput
from django.core import validators
from MyApp.models import User

class FormName(forms.ModelForm):
    first_name = forms.CharField(validators=[validators.MinLengthValidator(3)])
    class Meta:
        model=User
        fields='__all__'
        # exclude=['first_name']
        # fields=['first_name']

# class FormName(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email_id = forms.EmailField()
    # verify_email = forms.EmailField()
    # botcatcher = forms.CharField(required=False,widget=HiddenInput,validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatch = self.cleaned_data['botcatcher']
    #     if len(botcatch)>0:
    #         raise forms.ValidationError('Bot detected')
    #
    # def clean_first_name(self):
    #     first = self.cleaned_data['first_name']
    #     if first[0].lower() !='z':
    #         raise forms.ValidationError('First Name should start with Z')
    #     return first

    # def clean(self):
    #     get_all = super().clean()
    #     if get_all['email_id']!=get_all['verify_email']:
    #         raise forms.ValidationError("Emails do not match!")