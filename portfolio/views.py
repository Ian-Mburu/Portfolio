from django.shortcuts import render, get_object_or_404, redirect
from .models import CreateProject, Review, Blogs

from django.core.mail import send_mail
from .forms import ContactForm, ReviewForm
from django.conf import settings


# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def projects(request):
    projects = CreateProject.objects.all()
    return render(request, 'base/projects.html', {'projects': projects})

def projectDetails(request, pk):
    # Correctly reference the CreateProject model
    project = get_object_or_404(CreateProject, pk=pk)
    
    context = {
        'project': project
    }
    return render(request, 'base/project-details.html', context)

def contact(request):
    return render(request, 'base/contact.html')
    

def send_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract the form fields
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Compose the email message
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Send the email
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,  # From
                ['ianongaruiya@gmail.com'],    # To
                fail_silently=False
            )

            # Redirect to the contact page
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'base/contact.html', {'form': form})


def download(request):
    return render(request, 'base/download.html')

def reviews(request):
    all_reviews = Review.objects.all().order_by('-created_at')
    form = ReviewForm()
    return render(request, 'base/reviews.html', {'reviews': all_reviews, 'form': form})


def reviews(request):
    # Handle form submission
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('home')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = ReviewForm()

    # Fetch all reviews
    all_reviews = Review.objects.all().order_by('-created_at')

    return render(request, 'base/reviews.html', {'form': form, 'reviews': all_reviews})




def reviewsDetails(request, pk):
    # Correctly reference the CreateProject model
    review = get_object_or_404(Review, pk=pk)
    
    all_reviews = Review.objects.all()
   
    return render(request, 'base/reviewsDetails.html', { 'review': review})


# Blog
def blog(request):
    blogs = Blogs.objects.all()
    return render(request, 'base/blog.html', {'blogs': blogs})

def blogDetails(request, pk):
    # Correctly reference the CreateProject model
    blog = get_object_or_404(Blogs, pk=pk)

    return render(request, 'base/blogDetails.html', { 'blog': blog})


def portfolio_view(request):
    # Send an email notification whenever someone visits the portfolio page
    send_mail(
        subject='Portfolio Visit Alert',  # Email subject
        message='Someone just visited your portfolio!',  # Email message content
        from_email=settings.EMAIL_HOST_USER,  # From email (configured in settings)
        recipient_list=['ianongaruiya@gmail.com'],  # Recipient's email (where you want to get the notification)
        fail_silently=False,  # Raise an error if it fails
    )

    # Render your portfolio template
    return render(request, 'home.html')