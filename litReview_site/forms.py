from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Ticket, Review, UserFollows


class NewUserForm(UserCreationForm):

    """
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': "Enter your User Name"}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={"placeholder": "Enter your Password"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={"placeholder": "Confirm your Password"}))
"""
    class Meta:
        """
        """
        model = User
        fields = ("username", "password1", "password2")


class NewTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {
            "title": "Title",
            "description": "Description",
            "image": "Picture"
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

        }


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        labels = {
            "rating": "Rating",
            "headline": "Title",
            "body": "Content",
        }
        CHOICE = [('0', 0), ('1', 1), ('2', 2),
                  ('3', 3), ('4', 4), ('5', 5)]
        widgets = {
            'headline': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'rating': forms.RadioSelect(
                choices=CHOICE,
                attrs={
                    'class': 'custom-li',
                }
            )
        }


class UserFollowForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ['user', 'followed_user']
