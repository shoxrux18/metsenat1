<<<<<<< HEAD
from .serializers import StudentRegisterSerializer
from .models import Student
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
=======
from rest_framework.response import Response

from .serializers import StudentRegisterSerializer, StudentListSerializer
from .models import Student, Sponsor
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django_filters.rest_framework import DjangoFilterBackend
from .filter import FilterStudent
from rest_framework.permissions import IsAuthenticated
>>>>>>> b4f84d110abac91e3e728c058c03343c18dccad5

class StudentRegisterView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRegisterSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def perform_create(self, serializer):
<<<<<<< HEAD
        serializer.save(user=self.request.user)
=======
        serializer.save(user=self.request.user)


class StudentListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer




class StudentListViews(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = FilterStudent

    def get_queryset(self):
        user = self.request.user.is_authenticated
        if user:
            univer = self.kwargs['pk']
            student = Student.objects.filter(university_id=univer).all()
            return student
        return Response(data={
            "user_id": "you need register"
        })

    # def get_object(self):
    #     queryset = Student.objects.all()
    #     print(self.request)
        # for i in self.request:
        #     print(i)

        # make sure to catch 404's below
        # obj = Student.objects.filter(university_id=s)
        # print(obj)
        # self.check_object_permissions(self.request, obj)
        # return obj


>>>>>>> b4f84d110abac91e3e728c058c03343c18dccad5
