from django import forms


class BookGuestForm(forms.Form):
    name = forms.CharField(max_length=20, required=True, label='name')
    content = forms.CharField(max_length=300, required=True, label='content')
    email = forms.EmailField(required=True, label='email')
