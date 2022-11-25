from django.db.models import Model, CharField,ForeignKey,ImageField,DateField,EmailField,IntegerField, CASCADE, SET_NULL, ManyToManyField, FileField, BooleanField
from parent.models import Parent as P_p
from address.models import Location
from student.utils import RefTable, ref_table_verbose
from django.utils.translation import gettext as _

@ref_table_verbose(_('Gender '), _('Genders'))
class Gender(RefTable): pass

@ref_table_verbose(_('Level '), _('Levels'))
class SchoolLevel(RefTable): pass

@ref_table_verbose(_('Type of Disability'), _('Types of Disabilities '))
class SPNType(RefTable): pass

@ref_table_verbose(_('Grade '), _('Grades') )
class Grade(RefTable): pass

@ref_table_verbose(_('Year '), _('Years'))
class Year(RefTable): pass

@ref_table_verbose(_('Shift '), _('Shifts'))
class Shift(RefTable): pass

@ref_table_verbose(_('SchoolGender '), _('SchoolGenders'))
class SchoolGender(RefTable): pass

@ref_table_verbose(_('Relation'), _('Relations'))
class Relation(RefTable): pass


class School(Model):
    school_code = IntegerField(verbose_name= _('school code'), primary_key=True, null=False, blank=True)
    name = CharField(verbose_name= _('school name'),max_length=45, unique=True, null=True, blank=True)
    address = ForeignKey(Location, verbose_name=_('address'), on_delete=CASCADE, null=True, blank=True)
    phone_no = CharField(verbose_name=_('phone number'), max_length=50, null=True, blank=True)
    school_gender = ForeignKey(SchoolGender, max_length=50, blank=True, null=True, on_delete=SET_NULL)
    shift = ForeignKey(Shift, max_length=50, blank=True, null=True, on_delete=SET_NULL)
    levels = ManyToManyField(SchoolLevel, related_name='school')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = _('school')
        verbose_name_plural = _('schools')

class Document(Model):
    birth_certificate = FileField(upload_to='documents/', blank=True)
    release_letter = FileField(upload_to='documents/', blank=True)
    testimonial = FileField(upload_to='documents/', blank=True)
    marksheet = FileField(upload_to='documents/', blank=True)
    stipen_certificate = FileField(upload_to='documents/', blank=True)
    other_certificate = FileField(upload_to='documents/', blank=True)

    class Meta:
        verbose_name        = _('document')
        verbose_name_plural = _('documents')

class StudentInfo(Model):
    emis_id = IntegerField(_('Emis id'),primary_key=True ,blank=True, null=False)
    name = CharField(_('name'),max_length=100)
    photo = ImageField(_('student photo'),upload_to='student-photos/', blank=True, null=True)
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
    blood_group = CharField(_('blood group'),choices=blood_group_choice, max_length=5,  blank=True, null=True)
    date_of_birth = DateField(_('date of birth'), null=True)
    gender = ForeignKey(Gender, max_length=50, blank=True,  null=True, on_delete=SET_NULL)
    year =  ForeignKey(Year, max_length=10 , blank=True,  null=True, on_delete=SET_NULL)
    shift = ForeignKey(Shift, max_length=50, blank=True, null=True, on_delete=SET_NULL)
    spn_type = ForeignKey(SPNType, max_length=10 , blank=True,  null=True, on_delete=SET_NULL)
    phone_no = CharField(verbose_name=_('phone number'), max_length=11, blank=True, null=True)
    email = EmailField(_('email'), null=True,  blank=True)
    father_job = CharField(verbose_name=_('father jop'), max_length=50, null=True, blank=True)
    father_monthly_income = IntegerField(verbose_name=_('father monthly income'), null=True, blank=True)
    parent = ForeignKey(P_p,  null=True, blank=True, on_delete=SET_NULL)
    relation = ForeignKey(Relation, max_length=50, null=True, blank=True, on_delete=SET_NULL)
    address = ForeignKey(Location, null=True, blank=True, on_delete=SET_NULL)
    documents = ForeignKey( Document,  null=True, blank=True, on_delete=SET_NULL)
    school = ForeignKey(School,  null=True, blank=True, on_delete=SET_NULL)
    grade = ForeignKey(Grade, max_length=50, null=True, blank=True, on_delete=SET_NULL)
    checked = BooleanField(verbose_name=_('checking'), default=False)
    added_date = DateField(verbose_name=_('Add date '), auto_now_add=True)
    note = CharField(verbose_name=_('Note'), max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name        = _('Student')
        verbose_name_plural = _('Students')

