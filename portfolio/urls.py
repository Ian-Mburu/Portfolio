from django.urls import path
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>/', views.projectDetails, name='project-details'),
    path('contact/', views.send_message, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blogDetails/<int:pk>/', views.blogDetails, name='blogDetails'),
    path('download-resume/', views.download, name='download'),
    path('reviews/', views.reviews, name='reviews'),
    path('reviewDetails/<int:pk>/', views.reviewsDetails, name='reviewsDetails'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
