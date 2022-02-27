from django import forms

from leads.models import Lead


class LeadCreateForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=0)



class LeadCreateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'age', 'agent']