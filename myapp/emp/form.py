from socket import fromshare
from django import forms

class FeedbackForm(forms.Form):
    email=forms.EmailField(label="Enter you email",max_length=100)
    name=forms.CharField(label="Enter you name",max_length=100)
    feedback=forms.CharField(label="Your feedback",widget=forms.Textarea)
