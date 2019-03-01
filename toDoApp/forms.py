from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class toDoForm(forms.Form):
    text = forms.CharField(max_length=150,widget=forms.TextInput( attrs={'class':'form-control','placeholder':'Enter todo e.g. Delete junk files', 'aria-label':'Todo','aria-describedby':'add-btn'} ))

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user