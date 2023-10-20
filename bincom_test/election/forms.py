from django import forms
from .models import polling_unit, lga, announced_pu_results, party

class PollingUnitForm(forms.Form):
    p_units = polling_unit.objects.all()
    choices = [(p_unit.uniqueid, p_unit.polling_unit_name) for p_unit in p_units]
    polling_unit = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'class': 'form-control'}))


class LGAForm(forms.Form):
    lgas = lga.objects.all()
    choices = [(l.lga_id, l.lga_name) for l in lgas]
    LGA = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'class': 'form-control'}))


class PollingUnitResultForm(forms.Form):
    p_units = polling_unit.objects.all()
    choices = [(p_unit.uniqueid, p_unit.polling_unit_name) for p_unit in p_units]
    parties = party.objects.all()
    p_choices = [(_party.partyid, _party.partyname) for _party in parties]
    polling_unit = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'class': 'form-control'}))
    agent = forms.CharField(required=False)
    party = forms.ChoiceField(choices=p_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    score = forms.CharField()