from django.urls import path
from  .import views

app_name='basic_app'


urlpatterns=[
    path('orgname',views.orgname,name='orgname'),
    #path('sucessfull/',views.login,name='login'),
]
