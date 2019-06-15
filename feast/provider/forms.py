
from django import forms
from .models import Kitchen, Menu
from .models import Provider
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.ImageField()



class ProviderForm(forms.ModelForm):
	class Meta:
		model = Provider
		fields = ('provider_name','provider_email','provider_password','confirm_prov_password')


class KitchenForm(forms.ModelForm):
    class Meta:
        model = Kitchen
        fields = ('Mon','Tue','Wed','Thu','Fri','Sat','Sun','start_time','end_time')

class MenuForm(forms.ModelForm):
    class Meta:
        model= Menu
        fields = ('meal','vegetarian','price')