from . import views
from django.urls import path

urlpatterns = [

    # path('', views.main, name='main'),
    # path('research/', views.about, name='research'),
    # path('call/', views.contact, name='contact'),
    # path('get_det/', views.details, name='get_det'),
    # path('thanks/', views.end, name='thanks')

    # path('', views.main1, name='main1'),
    # path('res/', views.addition, name='addition')
    path('',views.main2,name='main2'),

]
