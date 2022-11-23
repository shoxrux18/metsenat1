from django.urls import path
from . import views

urlpatterns = [
    path('register-student/', views.StudentRegisterView.as_view()),
    path('register-sponsor/', views.SponsorRegisterView.as_view()),
    path('student/', views.StudentListView.as_view()),
    path('university/<int:pk>/students/', views.UniversityStudentsView.as_view()),
]