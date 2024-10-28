from . import views
from django.urls import path

app_name = 'eweb'

urlpatterns = [
    path('',views.anasayfa,name='anasayfa'),
    path('urunadd/',views.urunadd,name='urunadd'),
    path('urunlist/',views.urunlistt,name='urunlistt'),
    path('deleteurun/<int:id>',views.urunsil,name="urunsil")
]