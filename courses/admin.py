from django.contrib import admin
from .models import Category, Instructor, Course, Lesson, Enrollment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "title")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "instructor", "price_cents", "students", "rating")
    list_filter = ("category",)
    search_fields = ("title", "short_description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("course", "order", "title")
    list_filter = ("course",)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "created_at")
    list_filter = ("course",)

# Register your models here.
