from django.conf.urls import include, url
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^treenav/', include('treenav.urls')),
    # Catch all URL to easily demonstrate treenav display
    url(r'^', TemplateView.as_view(template_name='base.html')),
]
