from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('electronics',views.electronics,name='electronics'),
    path('fashion',views.fashion,name='fashion'),
    path('watche_ornaments',views.watche_ornaments,name='watche_ornaments'),
    path('mens_fashion',views.mens_fashion,name='mens_fashion'),
    path('womens_fashion',views.womens_fashion,name='womens_fashion')
]