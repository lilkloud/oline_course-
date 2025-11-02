from django.shortcuts import render
from django.db.models import Count, Avg, Q
from courses.models import Course, Instructor, Category, Enrollment


def home(request):
    # Get popular courses (most enrolled)
    popular_courses = Course.objects.filter(is_published=True).annotate(
        enrollment_count=Count('enrollments')
    ).order_by('-enrollment_count')[:6]
    
    # Get featured categories with course counts
    categories = Category.objects.annotate(
        course_count=Count('courses', filter=models.Q(courses__is_published=True))
    ).filter(course_count__gt=0).order_by('-course_count')[:8]
    
    # Get top instructors
    top_instructors = Instructor.objects.annotate(
        course_count=Count('courses', filter=models.Q(courses__is_published=True)),
        avg_rating=Avg('courses__rating')
    ).filter(course_count__gt=0).order_by('-course_count')[:4]
    
    # Get testimonials (you can replace this with a real Testimonial model later)
    testimonials = [
        {
            'name': 'Sarah Johnson',
            'role': 'Web Developer',
            'content': 'The courses on 9kloud helped me transition into a new career in web development. The instructors are knowledgeable and the content is up-to-date.',
            'avatar': 'https://randomuser.me/api/portraits/women/44.jpg'
        },
        {
            'name': 'Michael Chen',
            'role': 'Data Scientist',
            'content': 'I\'ve taken multiple courses here and each one has exceeded my expectations. The platform is easy to use and the support team is very responsive.',
            'avatar': 'https://randomuser.me/api/portraits/men/32.jpg'
        },
        {
            'name': 'Emily Rodriguez',
            'role': 'UX Designer',
            'content': 'As a busy professional, I appreciate the flexibility of learning at my own pace. The quality of instruction is top-notch and the community is very supportive.',
            'avatar': 'https://randomuser.me/api/portraits/women/68.jpg'
        }
    ]
    
    context = {
        'popular_courses': popular_courses,
        'categories': categories,
        'top_instructors': top_instructors,
        'testimonials': testimonials,
        'total_students': Enrollment.objects.values('user').distinct().count(),
        'total_courses': Course.objects.filter(is_published=True).count(),
        'total_instructors': Instructor.objects.annotate(
            course_count=Count('courses', filter=models.Q(courses__is_published=True))
        ).filter(course_count__gt=0).count(),
    }
    
    return render(request, 'home.html', context)


def teachers(request):
    instructors = Instructor.objects.all()
    return render(request, 'teachers_page.html', {"instructors": instructors})

# Create your views here.
