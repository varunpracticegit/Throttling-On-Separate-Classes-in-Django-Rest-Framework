from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.generics import (ListAPIView, CreateAPIView, 
RetrieveAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework.throttling import ScopedRateThrottle


#------------------------List objects API ------------------------------

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

# ----------------------Create objects API-------------------------------

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]  
    throttle_scope = 'modifystu'  

# ----------------------Get/Read objects API-----------------------------

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

# ----------------------Update objects API----------------------------

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'  

# ---------------------Delete objects API-----------------------------

class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'  

