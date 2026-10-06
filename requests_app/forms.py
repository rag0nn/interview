from django import forms

from .models import ServiceRequest


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['name', 'email', 'service', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'autocomplete': 'name',
                'placeholder': 'Adınız ve soyadınız',
                'minlength': 2,
                'maxlength': 100,
            }),
            'email': forms.EmailInput(attrs={
                'autocomplete': 'email',
                'placeholder': 'ornek@eposta.com',
                'maxlength': 254,
            }),
            'service': forms.Select(),
            'description': forms.Textarea(attrs={
                'placeholder': 'Projenizden, hedefinizden ve zaman planınızdan bahsedin.',
                'minlength': 20,
                'maxlength': 1500,
                'rows': 4,
            }),
        }

    def clean_name(self):
        name = ' '.join(self.cleaned_data['name'].split())
        if len(name) < 2:
            raise forms.ValidationError('Ad soyad en az 2 karakter olmalı.')
        return name

    def clean_description(self):
        description = self.cleaned_data['description'].strip()
        if len(description) < 20:
            raise forms.ValidationError('Açıklama en az 20 karakter olmalı.')
        return description