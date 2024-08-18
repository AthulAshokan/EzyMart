
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('',views.index,name="home_page"),
    path('product_list',views.product_list,name="product_list"),
    path('product_detail/<pk>',views.product_detail,name="product_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)