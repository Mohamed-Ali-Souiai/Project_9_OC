# blog/forms.py
from django import forms
from django.contrib.auth import get_user_model


import blog.models

User = get_user_model()

CHOICES = ((1, '-1'), (2, '-2'), (3, '-3'), (4, '-4'), (5, '-5'))


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(required=True, choices=CHOICES,
                             widget=forms.RadioSelect(attrs={'class': 'Radio'}))  # ,initial=1

    class Meta:
        model = blog.models.Review
        fields = ['headline', 'body', 'rating']


class TicketForm(forms.ModelForm):
    class Meta:
        model = blog.models.Ticket
        fields = ['title', 'description', 'image']


class UserFollowsForm(forms.Form):
    username = forms.CharField(max_length=50)

    def save(self):
        pass#  UserFollows.objects.create


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


"""**********************************************"""





class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)




