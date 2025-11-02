from django.urls import path
from django.views.generic import TemplateView
from .views import home, teachers

urlpatterns = [
    path('', home, name='home'),
    path('about', TemplateView.as_view(template_name='about_page.html'), name='about'),
    path('teachers', teachers, name='teachers'),
    path('contact', TemplateView.as_view(template_name='contact_page.html'), name='contact'),
]
