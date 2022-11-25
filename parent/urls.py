from django.urls import path

from .views import parent_delete, parent_edit, parent_profile, parents_list
urlpatterns = [
    path('list', parents_list, name='parents-list'),
    path('profile/<id>', parent_profile, name='parent-profile'),
    path('edit/<id>', parent_edit, name='parent-edit'),
    path('delete/<id>', parent_delete, name='parent-delete'),
]
