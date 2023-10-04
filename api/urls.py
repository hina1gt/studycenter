from django.urls import path, include
from .views import *

urlpatterns = [
    path('center/', studycenter),
    path('center/<int:pk>/', studycenter_detail),
    path('teacher/', teacher),
    path('teacher/<int:pk>/', teacher_detail),
    path('student/', student),
    path('student/<int:pk>/', student_detail),

    path('auth/', include('dj_rest_auth.urls')),
]