from django.forms import ModelForm,Select,TextInput,ClearableFileInput,DateInput,ModelChoiceField,IntegerField,NumberInput,Form,BooleanField,FileInput
from .models import Location, School, Document, StudentInfo, P_p
from address.models import Location
from django.utils.translation import gettext as _

class StudentAddressForm(ModelForm):
    class Meta:
        model = Location
        exclude = ['location_type','parent','notes','name']
        fields = ['governorate', 'district', 'sub_district', 'village', 'sub_village']
        widgets = {
            'governorate': Select(attrs={'class': 'form-control'}),
            'district': Select(attrs={'class': 'form-control'}),
            'sub_district': Select(attrs={'class': 'form-control'}),
            'village': Select(attrs={'class': 'form-control'}),
            'sub_village': Select(attrs={'class': 'form-control'})
        }

class  StudentForm(ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'
        exclude = ['added_date','checked','documents','address','parent']
        widgets = {
            'emis_id': TextInput(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'photo': ClearableFileInput(attrs={'class': 'form-control'}),
            'blood_group': Select(attrs={'class': 'form-control'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'gender': Select(attrs={'class': 'form-control', 'label':_('gender')}),
            'spn_type': Select(attrs={'class': 'form-control'}),
            'phone_no': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'father_job': TextInput(attrs={'class': 'form-control'}),
            'father_yearly_income': TextInput(attrs={'class': 'form-control'})
        }

class ChechForm(Form):
    class Meta:
        model = StudentInfo
        fields = ['checked']

class StudentSchoolForm(ModelForm):
    class Meta:
        model = School
        exclude = ['name', 'phone_no']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'disable': True }),
            'phone_no': TextInput(attrs={'class': 'form-control' })
        }

class StudentParentForm(ModelForm):
    class Meta:
        model = P_p
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'photo': ClearableFileInput(attrs={'class': 'form-control'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'place_of_birth': TextInput(attrs={'class': 'form-control'}),
            'blood_group': Select(attrs={'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-control'}),
            'id_type': Select(attrs={'class': 'form-control'}),
            'id_file': FileInput(attrs={'class': 'form-control'}),
            'phone_no': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
        }
        

class StudentDocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


