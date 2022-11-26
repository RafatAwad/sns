from django.urls import path
from .views import student_delete,student_edit,student_list,student_profile,student_registration,sch_delete,sch_profile,schools_list,print_form

urlpatterns = [
        path('schools-list', schools_list, name='schools-list'),
        path('sch-profile/<school_code>', sch_profile, name='school-profile'),
        #path('sch-edit', sch_edit, name='school-edit'),
        path('sch-delete/<school_code>', sch_delete, name='school-delete'),
        path('student-list', student_list, name='student-list'),
        path('student-registration', student_registration, name='student-registration'),
        path('profile/<emis_id>', student_profile, name='student-profile'),
        path('edit/<emis_id>', student_edit, name='student-edit'),
        path('delete/<emis_id>', student_delete, name='student-delete'),
        path('printf/', print_form, name='printf'),



]
