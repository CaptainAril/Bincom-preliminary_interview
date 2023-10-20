from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import View

from .models import polling_unit, announced_pu_results, lga
from .forms import PollingUnitForm, LGAForm, PollingUnitResultForm

# Create your views here.

def index(request):
    """Home page view"""
    context  = {'name':'Emmanuel Obe'}
    return render(request, 'index.html', context=context)

class UnitResultView(View):
    """Polling Unit Result Fetch view"""
    def get(self, request, *args, **kwargs):
        form = PollingUnitForm()
        return render(request, 'poll_unit.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = PollingUnitForm(request.POST)
        if form.is_valid():
            p_unit_id = form.cleaned_data['polling_unit']
            unit = polling_unit.objects.get(uniqueid=p_unit_id)
            pu_results = announced_pu_results.objects.filter(polling_unit_uniqueid=p_unit_id)
        return render(request, 'pu_results.html', {'pu_unit':unit, 'results':pu_results})
    

class LGAResultView(View):
    """LGA Results View"""
    def get(self, request, *args, **kwargs):
        form = LGAForm()
        return render(request, 'lga.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = LGAForm(request.POST)
        if form.is_valid():
            lga_id = form.cleaned_data['LGA']
            LGA = lga.objects.get(lga_id=lga_id)
            polling_units = polling_unit.objects.filter(lga=LGA.lga_id)

            # Compute total LGA votes by party
            results = {}
            for unit in polling_units:
                _results = announced_pu_results.objects.filter(polling_unit_uniqueid=unit.uniqueid)
                for result in _results:
                    
                    party = getattr(result, 'party_abbreviation')
                    score = getattr(result, 'party_score')
                    if party not in results:
                        results[party] = 0
                    results[party] += int(score)

        return render(request, 'lga_results.html', {'lga':LGA, 'results':results})
    

class AddPollResultView(View):
    """Add/Update Polling Unit Vote Counts"""
    def get(self, request, *args, **kwargs):
        form = PollingUnitResultForm()
        return render(request, 'add_pu_result.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        
        form = PollingUnitResultForm(request.POST)
        if form.is_valid():
            p_unit_id = form.cleaned_data['polling_unit']
            agent = form.cleaned_data['agent']
            party = form.cleaned_data['party']
            score = form.cleaned_data['score']
            unit = polling_unit.objects.get(uniqueid=p_unit_id)
            

            new_pu_result, created = announced_pu_results.objects.get_or_create(
                polling_unit_uniqueid=unit.uniqueid,
                party_abbreviation=party,
                defaults={'entered_by_user':agent, 'party_score':score}
            )

            if not created:
                new_pu_result.entered_by_user = agent
                new_pu_result.party_score = score
                new_pu_result.save()

        return redirect('new_result')
