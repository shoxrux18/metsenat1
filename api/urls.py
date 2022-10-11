from django.urls import path
from .views import StudentRegisterView, StudentListView, StudentListViews,SponsorRegisterView

urlpatterns = [
    path('register-student/', StudentRegisterView.as_view(), name='register-student'),
    path('list-student/', StudentListView.as_view(), name='list_student'),
    path('list-students/<int:pk>/', StudentListViews.as_view(), name='list_students'),
    path('register-sponsor/', SponsorRegisterView.as_view(), name='register-student'),
]