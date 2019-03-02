from django import forms
from .models import Supply, Demand , DrugStock

class DrugStockerForm(forms.ModelForm):
	class Meta:
		model = DrugStock
		fields = ['stocker_type','name','address',]
	

class SupplyForm(forms.ModelForm):
	class Meta:
		model = Supply
		fields = ['address']


class DemandForm(forms.ModelForm):
	class Meta:
		model = Demand
		fields = '__all__'
