from django.db import models
from django.utils import timezone

class ContactMessage(models.Model):
    """Modelo para mensagens do formulário de contacto."""
    SUBJECT_CHOICES = [
        ('general', 'Informações Gerais'),
        ('support', 'Suporte Técnico'),
        ('sales', 'Vendas e Orçamentos'),
        ('partnership', 'Parcerias'),
        ('other', 'Outro Assunto'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")
    company = models.CharField(max_length=100, blank=True, null=True, verbose_name="Empresa")
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='general', verbose_name="Assunto")
    message = models.TextField(verbose_name="Mensagem")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Envio")
    is_read = models.BooleanField(default=False, verbose_name="Lido")
    
    class Meta:
        verbose_name = "Mensagem de Contacto"
        verbose_name_plural = "Mensagens de Contacto"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.get_subject_display()} - {self.created_at.strftime('%d/%m/%Y')}"
    
    def mark_as_read(self):
        """Marca a mensagem como lida."""
        self.is_read = True
        self.save()


class MeetingRequest(models.Model):
    """Modelo para solicitações de reunião."""
    MEETING_TYPE_CHOICES = [
        ('online', 'Reunião Online'),
        ('in_person', 'Reunião Presencial'),
        ('phone', 'Chamada Telefónica'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Telefone")
    company = models.CharField(max_length=100, verbose_name="Empresa")
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cargo")
    meeting_type = models.CharField(max_length=20, choices=MEETING_TYPE_CHOICES, default='online', verbose_name="Tipo de Reunião")
    preferred_date = models.DateField(verbose_name="Data Preferencial")
    preferred_time = models.TimeField(verbose_name="Hora Preferencial")
    alternative_date = models.DateField(blank=True, null=True, verbose_name="Data Alternativa")
    alternative_time = models.TimeField(blank=True, null=True, verbose_name="Hora Alternativa")
    topic = models.CharField(max_length=200, verbose_name="Tópico da Reunião")
    additional_info = models.TextField(blank=True, null=True, verbose_name="Informações Adicionais")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Solicitação")
    status = models.CharField(max_length=20, 
                              choices=[
                                  ('pending', 'Pendente'),
                                  ('confirmed', 'Confirmada'),
                                  ('rescheduled', 'Reagendada'),
                                  ('cancelled', 'Cancelada'),
                                  ('completed', 'Realizada')
                              ],
                              default='pending',
                              verbose_name="Estado")
    
    class Meta:
        verbose_name = "Solicitação de Reunião"
        verbose_name_plural = "Solicitações de Reunião"
        ordering = ['-preferred_date', '-preferred_time']
    
    def __str__(self):
        return f"{self.name} - {self.get_meeting_type_display()} - {self.preferred_date.strftime('%d/%m/%Y')}"


class BudgetRequest(models.Model):
    """Modelo para solicitações de orçamento."""
    SERVICE_CHOICES = [
        ('sensors', 'Implementação de Sensores'),
        ('ai', 'Inteligência Artificial e Machine Learning'),
        ('automation', 'Automação de Processos'),
        ('monitoring', 'Sistemas de Monitorização'),
        ('custom', 'Solução Personalizada'),
        ('consulting', 'Consultoria'),
    ]
    
    BUDGET_RANGE_CHOICES = [
        ('under_5k', 'Menos de 5.000€'),
        ('5k_15k', 'Entre 5.000€ e 15.000€'),
        ('15k_30k', 'Entre 15.000€ e 30.000€'),
        ('30k_50k', 'Entre 30.000€ e 50.000€'),
        ('50k_100k', 'Entre 50.000€ e 100.000€'),
        ('over_100k', 'Mais de 100.000€'),
        ('not_defined', 'Não definido'),
    ]
    
    TIMEFRAME_CHOICES = [
        ('immediate', 'Imediato'),
        ('1_3_months', '1-3 meses'),
        ('3_6_months', '3-6 meses'),
        ('6_12_months', '6-12 meses'),
        ('more_than_year', 'Mais de 1 ano'),
        ('not_defined', 'Não definido'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Telefone")
    company = models.CharField(max_length=100, verbose_name="Empresa")
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cargo")
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES, verbose_name="Tipo de Serviço")
    project_description = models.TextField(verbose_name="Descrição do Projeto")
    budget_range = models.CharField(max_length=20, choices=BUDGET_RANGE_CHOICES, default='not_defined', verbose_name="Faixa de Orçamento")
    timeframe = models.CharField(max_length=20, choices=TIMEFRAME_CHOICES, default='not_defined', verbose_name="Prazo Desejado")
    additional_requirements = models.TextField(blank=True, null=True, verbose_name="Requisitos Adicionais")
    how_did_you_find_us = models.CharField(max_length=100, blank=True, null=True, verbose_name="Como nos encontrou?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Solicitação")
    status = models.CharField(max_length=20, 
                              choices=[
                                  ('pending', 'Pendente'),
                                  ('in_progress', 'Em Análise'),
                                  ('sent', 'Orçamento Enviado'),
                                  ('accepted', 'Orçamento Aceite'),
                                  ('rejected', 'Orçamento Rejeitado'),
                                  ('expired', 'Expirado'),
                              ],
                              default='pending',
                              verbose_name="Estado")
    
    class Meta:
        verbose_name = "Solicitação de Orçamento"
        verbose_name_plural = "Solicitações de Orçamento"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.get_service_type_display()} - {self.created_at.strftime('%d/%m/%Y')}"