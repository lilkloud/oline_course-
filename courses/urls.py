from django.urls import path
from .views import list_courses, course_detail, enroll_course, unenroll_course

urlpatterns = [
    path('', list_courses, name='courses_list'),
    path('<slug:slug>/', course_detail, name='course_detail'),
    path('<slug:slug>/enroll/', enroll_course, name='course_enroll'),
    path('<slug:slug>/unenroll/', unenroll_course, name='course_unenroll'),
]
