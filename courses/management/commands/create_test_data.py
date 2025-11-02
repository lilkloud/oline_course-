from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from courses.models import Category, Instructor, Course, Lesson, Enrollment
from faker import Faker
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Create test data for the application'

    def handle(self, *args, **options):
        fake = Faker()
        
        # Create admin user if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Created admin user (username: admin, password: admin123)'))
        
        # Get or create categories
        categories = ['Web Development', 'Data Science', 'Mobile Development', 'Design', 'Business', 'Marketing']
        created_categories = []
        for name in categories:
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={'slug': name.lower().replace(' ', '-')}
            )
            created_categories.append(category)
        self.stdout.write(self.style.SUCCESS(f'Found/created {len(created_categories)} categories'))
        
        # Create instructors
        instructors = []
        for _ in range(5):
            instructor = Instructor.objects.create(
                full_name=fake.name(),
                title=fake.job(),
                photo=f'img/team-{random.randint(1, 5)}.jpg'
            )
            instructors.append(instructor)
        self.stdout.write(self.style.SUCCESS(f'Created {len(instructors)} instructors'))
        
        # Create courses
        course_titles = [
            'Complete Python Bootcamp', 'Advanced JavaScript', 'Machine Learning A-Z', 
            'Web Development with Django', 'iOS App Development', 'Android App Development',
            'UI/UX Design Fundamentals', 'Digital Marketing Masterclass', 'Business Analytics',
            'Project Management Professional'
        ]
        
        for i, title in enumerate(course_titles):
            course = Course.objects.create(
                title=title,
                slug=f'slug-{i+1}',
                short_description=fake.sentence(),
                category=random.choice(created_categories),
                instructor=random.choice(instructors),
                cover_image=f'img/course-{random.randint(1, 5)}.jpg',
                duration_minutes=random.randint(60, 300),
                price_cents=random.choice([1999, 2999, 3999, 4999]),
                rating=round(random.uniform(3.5, 5.0), 1),
                students=random.randint(10, 1000)
            )
            
            # Create lessons for each course
            num_lessons = random.randint(5, 10)
            for j in range(num_lessons):
                Lesson.objects.create(
                    course=course,
                    title=f'Module {j+1}: {fake.sentence()}',
                    content='\n\n'.join(fake.paragraphs(nb=3)),
                    order=j+1
                )
            
            # Create some enrollments for the course
            num_enrollments = random.randint(0, 10)
            for _ in range(num_enrollments):
                user, created = User.objects.get_or_create(
                    username=fake.user_name(),
                    defaults={
                        'email': fake.email(),
                        'first_name': fake.first_name(),
                        'last_name': fake.last_name()
                    }
                )
                if created:
                    user.set_password('testpass123')
                    user.save()
                
                Enrollment.objects.get_or_create(user=user, course=course)
            
            self.stdout.write(self.style.SUCCESS(f'Created course: {title} with {num_lessons} lessons and {num_enrollments} enrollments'))
        
        self.stdout.write(self.style.SUCCESS('\nSuccessfully created test data!'))
        self.stdout.write(self.style.SUCCESS('\nAdmin URL: http://127.0.0.1:8000/admin/'))
        self.stdout.write(self.style.SUCCESS('Username: admin'))
        self.stdout.write(self.style.SUCCESS('Password: admin123'))
        self.stdout.write(self.style.SUCCESS('\nRegular user login:'))
        self.stdout.write(self.style.SUCCESS('Username: user1 (or user2, user3, etc.)'))
        self.stdout.write(self.style.SUCCESS('Password: testpass123'))
