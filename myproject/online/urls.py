from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'online'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)$', views.product_list, name='product_list_by_category'),
    url(r'^detail/(?P<id>\d+)$', views.product_detail, name='product_detail'),
    url(r'^loggin/validateuser', views.validateuser, name='validateuser'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)