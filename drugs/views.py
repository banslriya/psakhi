from django.shortcuts import render, redirect
from django.http import HttpResponse
from drugs.models import Drug
from drugs.models import DrugCategory , DrugStock
from .forms import DrugForm
from service.forms import SupplyForm
from django.urls import reverse

# Create your views here.
def medicine(request):
	return render(request,'drugs/medicine.html')

def donate_medicine(request):
	if not request.user.is_authenticated:
		return redirect(reverse('login'))
	else:
		if request.method == "POST":
			drug_form = DrugForm(request.POST)
			supply_form = SupplyForm(request.POST)
			if drug_form.is_valid() and supply_form.is_valid():
				supply_form.save(commit=False)
				drug_form.save(commit=False)
				supply_form.instance.donor = request.user
				supply = supply_form.save()
				drug_form.instance.supply = supply
				drug_form.save()			
			return redirect(reverse('home:home'))
		else:
			drug_form = DrugForm()
			supply_form = SupplyForm()
		return render(request,
			          'drugs/drug_donation.html', 
			          {'drug_form': drug_form,
			           'supply_form': supply_form,})










#def list(request):
#	results1 = Diseases.objects.all()
#	results2 = Drugs.objects.all()
#	return render(request,'riya/list.html', {"results1": results1,"results2":results2})







#def laboratory_medicine(request):
#	if request.user.is_authenticated:
#		#return redirect(reverse('medicine:medicines_list'))
#		pass
#	else:
#		return render(request,'registration/login.html')

#def sell_medicine(request):
#	if request.user.is_authenticated:
#		#return redirect(reverse('medicine:medicines_list'))
#		pass
#	else:
#		return render(request,'registration/login.html')



#def medicines_list(request):
#	f = MedicineFilter(request.GET, queryset=Medicine.objects.all())
#	return render(request,'buyer.html',{'filter':f})