from django import forms
 
class ProductForm(forms.Form):
    name = forms.CharField()
    cost = forms.IntegerField()