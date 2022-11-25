from django.contrib import admin
from django.urls import path, include
from .views import home_page
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('', home_page, name='home'),
    path('student/', include('student.urls')),
    path('parent/', include('parent.urls')),
    path('address/', include('address.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    
    # path('advanced_filters/', include('advanced_filters.urls'))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('captcha/', include('captcha.urls')),
]