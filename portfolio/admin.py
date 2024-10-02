from django.contrib import admin
from .models import CreateProject, Review, Blogs

# Register your models here.


admin.site.register(CreateProject)
admin.site.register(Review)
admin.site.register(Blogs)