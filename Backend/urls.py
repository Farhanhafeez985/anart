from django.urls import path, include
from Backend import views

urlpatterns = [
    path('', views.home, name="home"),
    path('gallery', views.gallery, name="gallery"),
    path('signup', views.Signup, name="signup"),
    path('contact', views.contact, name="contact"),
    path('project', views.project, name="project"),
    path('about', views.about, name="about"),
    path('blogs', views.blogs, name="blogs"),
]
