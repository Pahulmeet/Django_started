from django.conf.urls import url
from . import views

app_name = 'blood'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^request/$', views.DetailView.as_view(), name='detail'),


    url(r'^signup_donor/$',views.DonorRegister, name='signup_donor'),
    url(r'^signup_hospital/$',views.HospitalRegister, name='signup_hospital'),
    url(r'^request/$', views.BloodRequest, name='request'),

    url(r'^DonorProfile/$', views.ProfileDonor, name='P_donor'),
    url(r'^HospitalProfile/$', views.ProfileHospital, name='P_hospital'),

    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),

]