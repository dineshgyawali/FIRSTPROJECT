from django.urls import path

from . import views

urlpatterns = [
    path('h/', views.Hello, name='Hello'),
    path('w/', views.World, name='World'),
    path('x/', views.welcome, name='welcome'),
    path('y/', views.Attendanceview, name="AV"),
    path('y/z/', views.Submission, name="sub"),
    path('c/', views.Csview, name="CV"),
    path('s/', views.Staffview, name="SV"),
    path('su/', views.Supportview, name ="SP"),
    
]