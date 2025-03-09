from django.contrib import admin
from .models import ContactMessage, MeetingRequest, BudgetRequest

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('subject', 'is_read', 'created_at')
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 25
    
    actions = ['mark_as_read']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Marcar mensagens selecionadas como lidas"


@admin.register(MeetingRequest)
class MeetingRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'meeting_type', 'preferred_date', 'preferred_time', 'status', 'created_at')
    list_filter = ('meeting_type', 'status', 'preferred_date')
    search_fields = ('name', 'email', 'company', 'topic')
    readonly_fields = ('created_at',)
    date_hierarchy = 'preferred_date'
    list_per_page = 25
    
    fieldsets = (
        ('Informações do Solicitante', {
            'fields': ('name', 'email', 'phone', 'company', 'position')
        }),
        ('Detalhes da Reunião', {
            'fields': ('meeting_type', 'topic', 'additional_info')
        }),
        ('Agendamento', {
            'fields': ('preferred_date', 'preferred_time', 'alternative_date', 'alternative_time')
        }),
        ('Estado', {
            'fields': ('status', 'created_at')
        }),
    )


@admin.register(BudgetRequest)
class BudgetRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'service_type', 'budget_range', 'timeframe', 'status', 'created_at')
    list_filter = ('service_type', 'budget_range', 'timeframe', 'status')
    search_fields = ('name', 'email', 'company', 'project_description')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 25
    
    fieldsets = (
        ('Informações do Solicitante', {
            'fields': ('name', 'email', 'phone', 'company', 'position')
        }),
        ('Detalhes do Projeto', {
            'fields': ('service_type', 'project_description', 'additional_requirements')
        }),
        ('Informações Financeiras e Temporais', {
            'fields': ('budget_range', 'timeframe')
        }),
        ('Informações Adicionais', {
            'fields': ('how_did_you_find_us', 'status', 'created_at')
        }),
    )