from django import forms
  
# creating a form
class InputForm(forms.Form):
  
    Email= forms.CharField(max_length = 200)
    ContactId = forms.CharField(max_length = 200)
    Nickname = forms.CharField(max_length = 200)
  
 
