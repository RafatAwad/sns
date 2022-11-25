from django.urls import path
from .views import student_delete,student_edit,student_list,student_profile,student_registration

urlpatterns = [
        path('student-list', student_list, name='student-list'),
        path('student-registration', student_registration, name='student-registration'),
        path('profile/<emis_id>', student_profile, name='student-profile'),
        path('edit/<emis_id>', student_edit, name='student-edit'),
        path('delete/<emis_id>', student_delete, name='student-delete'),



]
