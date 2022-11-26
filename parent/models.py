from django.db.models import Model, CharField,ForeignKey,ImageField,DateField,EmailField,IntegerField, CASCADE, SET_NULL, ManyToManyField, FileField, BooleanField
from address.models import Location
from .utils import RefTable, ref_table_verbose
#from student.models import Gender
from django.utils.translation import gettext as _


@ref_table_verbose(_('ID Type '), _('ID Types') )
class IdType(RefTable): pass

class Parent(Model):
    name = CharField(max_length=45)
    photo = ImageField(upload_to='parents-photos/',blank=True, null=True)
    date_of_birth = DateField(verbose_name=_('date of birth') ,null=True)
    place_of_birth = CharField(verbose_name=_('Place of birth') ,max_length=45,blank=True, null=True)
    gender = ForeignKey('student.Gender', max_length=50, blank=True, null=True, on_delete=SET_NULL)
    blood_group_choice = (
        ('a+', 'A+'),
        ('o+', 'O+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),
        ('a-', 'A-'),
        ('o-', 'O-'),
        ('b-', 'B-'),
        ('ab-', 'AB-')
    )
    blood_group = CharField(choices=blood_group_choice, verbose_name=_('blood group'), max_length=5, blank=True, null=True)
    id_type = ForeignKey(IdType, max_length=50, null=True, on_delete=SET_NULL)
    id_file = FileField(upload_to='documents/', blank=True, verbose_name=_('id file'))
    phone_no = CharField(max_length=11, blank=True, null=True, verbose_name=_('phone number'))
    email = CharField(max_length=255,blank=True, null=True)
    address = ForeignKey(Location, verbose_name=_('place of live'), on_delete=SET_NULL,blank=True, null=True, related_name='parents')


    def __str__(self):
        return self.name
