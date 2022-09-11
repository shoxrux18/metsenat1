<<<<<<< HEAD
from django.urls import path
from .views import StudentRegisterView

urlpatterns = [
    path('register-student/',StudentRegisterView.as_view(),name='register-student')
=======
from django.urls import path, re_path
from .views import StudentRegisterView, StudentListView, StudentListViews

urlpatterns = [
    path('register-student/', StudentRegisterView.as_view(), name='register-student'),
    path('list-student/', StudentListView.as_view(), name='list_student'),
    path('list-students/<int:pk>/', StudentListViews.as_view(), name='list_students')
>>>>>>> b4f84d110abac91e3e728c058c03343c18dccad5
]