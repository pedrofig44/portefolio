from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ContactMessage, MeetingRequest, BudgetRequest

class ContactMessageForm(forms.ModelForm):
    """Formulário para mensagens de contacto."""
    
    # Redefino os campos para adicionar classes e placeholders
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'O seu nome completo'
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'O seu email'
        })
    )
    
    phone = forms.CharField(
        max_length=20, 
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'O seu telefone (opcional)'
        })
    )
    
    company = forms.CharField(
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'A sua empresa (opcional)'
        })
    )
    
    subject = forms.ChoiceField(
        choices=[('', 'Selecione o assunto')] + list(ContactMessage.SUBJECT_CHOICES),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
            'placeholder': 'A sua mensagem',
            'style': 'min-height: 120px;'
        })
    )
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'company', 'subject', 'message']

    def clean_phone(self):
        """Valida o formato do número de telefone."""
        phone = self.cleaned_data.get('phone')
        if phone:
            # Remove caracteres não numéricos
            phone_digits = ''.join(filter(str.isdigit, phone))
            if len(phone_digits) < 9:
                raise forms.ValidationError(_('Por favor, introduza um número de telefone válido.'))
        return phone
        
    def clean_subject(self):
        """Valida que o assunto foi selecionado."""
        subject = self.cleaned_data.get('subject')
        if subject == '':
            raise forms.ValidationError(_('Por favor, selecione um assunto.'))
        return subject

class MeetingRequestForm(forms.ModelForm):
    """Formulário para solicitações de reunião."""
    
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'O seu nome completo'
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'O seu email'
        })
    )
    
    phone = forms.CharField(
        max_length=20, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'O seu telefone'
        })
    )
    
    company = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'A sua empresa'
        })
    )
    
    position = forms.CharField(
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'O seu cargo (opcional)'
        })
    )
    
    meeting_type = forms.ChoiceField(
        choices=MeetingRequest.MEETING_TYPE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    preferred_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    preferred_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time'
        })
    )
    
    alternative_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    alternative_time = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time'
        })
    )
    
    topic = forms.CharField(
        max_length=200, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Assunto principal da reunião'
        })
    )
    
    additional_info = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Informações adicionais (opcional)'
        })
    )
    
    class Meta:
        model = MeetingRequest
        fields = ['name', 'email', 'phone', 'company', 'position', 
                 'meeting_type', 'preferred_date', 'preferred_time', 
                 'alternative_date', 'alternative_time', 'topic', 'additional_info']

    def clean_phone(self):
        """Valida o formato do número de telefone."""
        phone = self.cleaned_data.get('phone')
        if phone:
            # Remove caracteres não numéricos
            phone_digits = ''.join(filter(str.isdigit, phone))
            if len(phone_digits) < 9:
                raise forms.ValidationError(_('Por favor, introduza um número de telefone válido.'))
        return phone
    
    def clean_alternative_time(self):
        """Verifica se a hora alternativa está preenchida quando a data alternativa está preenchida."""
        alternative_date = self.cleaned_data.get('alternative_date')
        alternative_time = self.cleaned_data.get('alternative_time')
        
        if alternative_date and not alternative_time:
            raise forms.ValidationError(_('Por favor, introduza a hora alternativa.'))
        
        return alternative_time


class BudgetRequestForm(forms.ModelForm):
    """Formulário para solicitações de orçamento."""
    
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'O seu nome completo'
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'O seu email'
        })
    )
    
    phone = forms.CharField(
        max_length=20, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'O seu telefone'
        })
    )
    
    company = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'A sua empresa'
        })
    )
    
    position = forms.CharField(
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'O seu cargo (opcional)'
        })
    )
    
    service_type = forms.ChoiceField(
        choices=BudgetRequest.SERVICE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    project_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Descreva o seu projeto e as suas necessidades'
        })
    )
    
    budget_range = forms.ChoiceField(
        choices=BudgetRequest.BUDGET_RANGE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    timeframe = forms.ChoiceField(
        choices=BudgetRequest.TIMEFRAME_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    additional_requirements = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Requisitos adicionais ou detalhes específicos (opcional)'
        })
    )
    
    how_did_you_find_us = forms.CharField(
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Como tomou conhecimento dos nossos serviços? (opcional)'
        })
    )
    
    class Meta:
        model = BudgetRequest
        fields = ['name', 'email', 'phone', 'company', 'position', 'service_type', 
                 'project_description', 'budget_range', 'timeframe', 
                 'additional_requirements', 'how_did_you_find_us']

    def clean_phone(self):
        """Valida o formato do número de telefone."""
        phone = self.cleaned_data.get('phone')
        if phone:
            # Remove caracteres não numéricos
            phone_digits = ''.join(filter(str.isdigit, phone))
            if len(phone_digits) < 9:
                raise forms.ValidationError(_('Por favor, introduza um número de telefone válido.'))
        return phone