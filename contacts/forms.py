from django import forms
from django.core.validators import FileExtensionValidator
from .models import Contact

class ContactForm(forms.ModelForm):
    image = forms.ImageField(
        required=False,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
        widget=forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'})
    )

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'category', 'notes', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }