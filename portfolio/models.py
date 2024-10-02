from django.db import models

# Create your models here.


class CreateProject(models.Model):
    projectImage = models.ImageField(upload_to='project_images/', null=False, blank=False)
    projectName = models.CharField(max_length=200)
    projectTechnology = models.CharField(max_length=20, null=False, blank=False)
    projectDescription = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['projectName']

    def __str__(self):
        return self.projectName
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    

from django.contrib.auth.models import User

class Review(models.Model):
    image = models.ImageField(upload_to='project_images/', null=False, blank=False)
    name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.rating} stars'
    

class Blogs(models.Model):
    image = models.ImageField(upload_to='project_images/', null=False, blank=False)
    title = models.CharField(max_length=200)
    highlights = models.TextField(max_length=1000)
    contributions = models.TextField(max_length=1000)

    def __str__(self):
        return self.title