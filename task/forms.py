from django import forms
from .models import ProjectTask

class ProjectTaskForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    
    class Meta:
        model = ProjectTask
        fields = ['date', 'project', 'project_code', 'activity', 'estimated_hours', 'status']
        widgets = {
            'project': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'project_code': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'activity': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control'
            }),
            'estimated_hours': forms.NumberInput(attrs={
                'step': '0.5',
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            })
        }