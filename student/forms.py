from django.forms import ModelForm,Select,TextInput,ClearableFileInput,DateInput,ModelChoiceField,IntegerField,NumberInput,Form,BooleanField,FileInput,CheckboxInput
from .models import Location, School, Document, StudentInfo, P_p
from address.models import Location
from django.utils.translation import gettext as _

class StudentAddressForm(ModelForm):
    class Meta:
        model = Location
        fields = ['governorate', 'district', 'sub_district', 'village', 'sub_village']
        widgets = {
            'governorate': Select(attrs={'class': 'form-control'}),
            'district': Select(attrs={'class': 'form-control'}),
            'sub_district': Select(attrs={'class': 'form-control'}),
            'village': Select(attrs={'class': 'form-control'}),
            'sub_village': Select(attrs={'class': 'form-control'})
        }
        labels = {
            "governorate": _('governorate'),
            "district":  _('district'),
            "sub_district":  _('sub district'),
            "village":  _('village'),
            "sub_village":  _('sub village'),
        }
class  StudentForm(ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'
        exclude = ['added_date','checked','documents','address','parent', 'email','phone_no']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'photo': ClearableFileInput(attrs={'class': 'form-control'}),
            'blood_group': Select(attrs={'class': 'form-control'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'gender': Select(attrs={'class': 'form-control'}),
            'spn_type': Select(attrs={'class': 'form-control'}),
            'shift': Select(attrs={'class': 'form-control'}),
            'year': Select(attrs={'class': 'form-control'}),
            'grade': Select(attrs={'class': 'form-control'}),
            'relation': Select(attrs={'class': 'form-control'}),
            'father_is_guard': CheckboxInput(attrs={'class': 'icheck-success'}),
            'father_job': TextInput(attrs={'class': 'form-control'}),
            'father_yearly_income': TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            "gender": _('gender'),
            "shift":  _('shift'),
            "spn_type":  _('Type of Disability'),
            "relation":  _('relation'),
            "school":  _('school'),
            "grade":  _('grade'),
            "school":  _('school'),
            "father_is_guard":  _('Is father the Gaurd ?'),
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
        labels = {
            "address": _('address'),
            "school_gender":  _('school gender'),
            "shift":  _('shift'),
            "levels":  _('levels'),
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
            'address': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            "photo": _('photo'),
            "blood_group": _('blood group'),
            "name":  _('name'),
            "gender":  _('gender'),
            "id_type":  _('id type'),
            "id_file":  _('id file'),
            "phone_no":  _('phone number'),
            "email":  _('email'),
            "address":  _('address'),
        }
class StudentDocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
