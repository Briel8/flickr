from django import forms

class UserIdForm(forms.Form):
    user_id = forms.CharField(required=True, min_length=10, max_length=100)