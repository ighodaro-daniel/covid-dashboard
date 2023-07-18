from django.urls import path
from . import views
urlpatterns=[
path('info',views.info_list,name='info'),
path('info/<str:location>/',views.info_list)
]