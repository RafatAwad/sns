from django.forms import ModelForm, TextInput,ClearableFileInput,DateInput,Select,EmailInput,NumberInput
from .models import Parent, Location

class ParentForm(ModelForm):
    class Meta:
        model = Parent
        exclude = ['address']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'photo': ClearableFileInput(attrs={'class': 'form-control'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'place_of_birth': TextInput(attrs={'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-control'}),
            'blood_group': Select(attrs={'class': 'form-control'}),
            'id_type': Select(attrs={'class': 'form-control'}),
            'id_file': ClearableFileInput(attrs={'class': 'form-control'}),
            'phone_no': NumberInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
        }


class ParentAddressForm(ModelForm):
    class Meta:
        model = Location
        fields = ('governorate', 'district', 'sub_district', 'village', 'sub_village')
        widgets = {
            'governorate': Select(attrs={'class': 'form-control'}),
            'district': Select(attrs={'class': 'form-control'}),
            'sub_district': Select(attrs={'class': 'form-control'}),
            'village': Select(attrs={'class': 'form-control'}),
            'sub_village': TextInput(attrs={'class': 'form-control'}),
        }
