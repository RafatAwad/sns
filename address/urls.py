from django.urls import path
from.views import load_school_entry


urlpatterns = [
         path('load-schools', load_school_entry, name='load-schools-entry'),

]
