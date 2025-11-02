from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Enrollment


def list_courses(request):
    qs = Course.objects.select_related('category', 'instructor').all()
    q = request.GET.get('q')
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, 'courses_list.html', {"courses": qs, "q": q or ''})


def course_detail(request, slug: str):
    course = get_object_or_404(Course.objects.select_related('category', 'instructor'), slug=slug)
    lessons = course.lessons.all()
    is_enrolled = False
    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
    return render(request, 'course_detail.html', {"course": course, "lessons": lessons, "is_enrolled": is_enrolled})


@login_required
def enroll_course(request, slug: str):
    if request.method != 'POST':
        return redirect(f'/courses/{slug}/')
    course = get_object_or_404(Course, slug=slug)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    messages.success(request, 'You are enrolled in this course.')
    return redirect(f'/courses/{slug}/')


@login_required
def my_courses(request):
    enrollments = (
        Enrollment.objects.select_related('course', 'course__instructor')
        .filter(user=request.user)
    )
    return render(request, 'my_courses.html', {"enrollments": enrollments})


@login_required
def unenroll_course(request, slug: str):
    if request.method != 'POST':
        return redirect(f'/courses/{slug}/')
    course = get_object_or_404(Course, slug=slug)
    Enrollment.objects.filter(user=request.user, course=course).delete()
    messages.info(request, 'You have unenrolled from this course.')
    return redirect(f'/courses/{slug}/')

# Create your views here.
