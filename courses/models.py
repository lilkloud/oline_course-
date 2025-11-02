from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Instructor(models.Model):
    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=120, blank=True)
    photo = models.CharField(max_length=255, blank=True, help_text="Path under /static/img e.g. img/team-1.jpg")

    def __str__(self):
        return self.full_name


class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="courses")
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, related_name="courses")
    cover_image = models.CharField(max_length=255, blank=True, help_text="Path under /static/img e.g. img/course-1.jpg")
    duration_minutes = models.PositiveIntegerField(default=90)
    price_cents = models.PositiveIntegerField(default=9900)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.5)
    students = models.PositiveIntegerField(default=25)
    short_description = models.TextField(blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=1)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}. {self.title}"


User = get_user_model()


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "course")

    def __str__(self):
        return f"{self.user} -> {self.course}"

# Create your models here.
