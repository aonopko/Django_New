from django import forms


from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'email-bt'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'email-bt'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'email-bt'}),
            'massage': forms.TextInput(attrs={'placeholder': 'Massage', 'class': 'massage-bt'})
        }
