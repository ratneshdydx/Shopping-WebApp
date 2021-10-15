from django.conf.urls import url
from . import views

urlpatterns=[
    #url(r'^adminhome$',views.adminhome,name='adminhome'),
    url(r'^adminhome$', views.adminhome, name='adminhome'),
    url(r'^(?P<category_slug>[-\w]+)$', views.adminhome, name='product_list_by_category_admin'),
    url(r'^detail/(?P<id>\d+)$', views.product_det, name='product_det'),
    url(r'^cart/add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^cart/remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^logout/$', views.logout, name='logout'),
]