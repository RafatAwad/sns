from enum import unique
from django.db.models import Model, CharField, ForeignKey, CASCADE, SET_NULL,TextField
from student.utils import RefTable, ref_table_verbose
from django.utils.translation import gettext as _

@ref_table_verbose(_('location type'), _('location types '))
class LocationType(RefTable): pass

class Governorate(Model):
    name = CharField(_('governorate') , max_length=45, unique=True, null=True, blank=True)
    gov_code = CharField(_('governorate code'), max_length=50, unique=True, null=True, blank=True)
    notes = CharField(_('notes'), max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class District(Model):
    name = CharField(_('district'), max_length=100, unique=True, null=True, blank=True)
    dist_code = CharField(_('district code'), max_length=50, null=True, blank=True)
    governorate = ForeignKey(Governorate, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class SubDistrict(Model):
    name = CharField(_('subdistrict'), max_length=100, unique=True, null=True, blank=True)
    sub_dist_code = CharField(_('subdistrict code'), max_length=50, null=True, blank=True)
    governorate = ForeignKey(Governorate,  on_delete=CASCADE, null=True, blank=True)
    district = ForeignKey(District, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Village(Model):
    name = CharField(_('village'),max_length=100, unique=True, null=True, blank=True)
    village_code = CharField(_('village code'), max_length=50, null=True, blank=True)
    governorate = ForeignKey(Governorate, on_delete=CASCADE, null=True, blank=True)
    district = ForeignKey(District, on_delete=CASCADE, null=True, blank=True)
    sub_district = ForeignKey(SubDistrict, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class SubVillage(Model):
    name = CharField(_('subvillage'),max_length=100, unique=True, null=True, blank=True)
    sub_village_code = CharField(_('subvillage code'), max_length=50, null=True, blank=True)
    governorate = ForeignKey(Governorate, on_delete=CASCADE, null=True, blank=True)
    district = ForeignKey(District, on_delete=CASCADE, null=True, blank=True)
    sub_district = ForeignKey(SubDistrict, on_delete=CASCADE, null=True, blank=True)
    village = ForeignKey(Village, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Location(Model):
    id                  = CharField(_('ID'), primary_key=True, max_length=100)
    location_type       = ForeignKey(LocationType, null=True, blank=True, on_delete=SET_NULL)
    name                = CharField(_('Name'), max_length=255, null=True, blank=True)
    governorate         = ForeignKey(Governorate, on_delete=SET_NULL, null=True, blank=True)
    district            = ForeignKey(District, on_delete=SET_NULL, null=True, blank=True)
    sub_district        = ForeignKey(SubDistrict, on_delete=SET_NULL, null=True, blank=True)
    village             = ForeignKey ( Village,on_delete=SET_NULL,null=True, blank=True)
    sub_village         = ForeignKey(SubVillage, on_delete=SET_NULL, null=True, blank=True)
    notes               = TextField(_('notes'), null=True, blank=True)

    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)

# class Location(Model):
#     id                  = CharField(_('ID'), primary_key=True, max_length=100)
#     location_type       = ForeignKey(LocationType, null=False, blank=False, on_delete=CASCADE, db_index=True)
#     name                = CharField(_('Name'), max_length=255, null=True, blank=True, db_index=True)
#     governorate         = ForeignKey(Governorate, on_delete=SET_NULL, max_length=10, null=True, blank=True, db_index=True)
#     district            = ForeignKey(District, on_delete=SET_NULL, max_length=10, null=True, blank=True, db_index=True)
#     sub_district        = ForeignKey(SubDistrict, on_delete=SET_NULL,  max_length=14, null=True, blank=True, db_index=True)
#     village             = ForeignKey(Village, on_delete=SET_NULL,  max_length=18, null=True, blank=True, db_index=True)
#     sub_village         = ForeignKey(SubVillage, on_delete=SET_NULL, max_length=22, null=True, blank=True, db_index=True)
#     notes               = TextField(_('notes'), null=True, blank=True)

#     def __str__(self):
#         return self.name
