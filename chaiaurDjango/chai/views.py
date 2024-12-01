from django.shortcuts import render
from .models import ChaiVariety, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.
def all_chai(request):
    chais = ChaiVariety.objects.all() #this will be a array
    return render(request, 'chai/all_chai.html', {'chais':chais})     #ye jo hia wo mereko ek html file return kr raha hai jo ki templates/website folder me hai


def chai_details(request, chai_id):
    chai= get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai':chai})


def chai_store_view(request):
    stores = None

    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety= form.cleaned_data['chai_variety']
            stores = Store.objects.filter(chai_varieties=chai_variety)

    else:
        form = ChaiVarietyForm()

    return render(request, 'chai/chai_stores.html', {'stores':stores, 'form':form})

