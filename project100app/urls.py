from django.urls import path
from . import views 

urlpatterns=[
        path('login/',views.user_login,name='login'),
        path('logout/',views.user_logout,name='logout'),
        path('create_account/',views.UserRegistration,name='create_account'),
        path('dashboard/<str:id>/',views.dashboard,name='dashboard'),
        path('doctor/',views.doctor,name="doctor"),
        path('patient/',views.patient,name="patient")
]