from django import forms
from django.core import validators

def start_with_v(value):
    if value[0].lower()!='v':
        raise forms.ValidationError('name should starts with v')
    
def name_len(value):
    if len(value)<=5:
        raise forms.ValidationError('name should be more than 5 charecters')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[start_with_v,name_len])
    age=forms.IntegerField(validators=[validators.MinValueValidator(18)])
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput,validators=[validators.MinLengthValidator(8)])
    botcatcher=forms.CharField(max_length=100,required=False,widget=forms.HiddenInput)
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])



    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']

        if e!=r:
            raise forms.ValidationError('email is not matched')
        else:
            pass

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('This not human')

