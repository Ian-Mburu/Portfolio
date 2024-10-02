from django import forms
from .models import ContactMessage
from .models import Review


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name', 
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your Email', 
                'class': 'form-control'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Subject', 
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your Message', 
                'class': 'form-control'
            }),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['image', 'name', 'review_text', 'rating']  # Include 'name'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'review_text': forms.Textarea(attrs={'placeholder': 'Write your review here...'}),
            'rating': forms.Select(choices=[(i, f'{i} stars') for i in range(1, 6)]),
}