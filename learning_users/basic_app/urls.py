from django.urls import path
from  .import views

app_name='basic_app'


urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),


    path('org/',views.org_base,name='org_base'),
    path('orgname/',views.orgname,name='orgname'),
    path('team/',views.Team_dic,name='Team_dic'),
    path('agile/',views.agile,name='agile'),
    path('emp/',views.emp,name='emp'),


]
