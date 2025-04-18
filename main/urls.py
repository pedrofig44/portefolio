from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),  # New FAQ route
    
    # Novas rotas
    path('meeting-request/', views.MeetingRequestView.as_view(), name='meeting_request'),
    path('meeting-request/success/', views.meeting_request_success, name='meeting_request_success'),
    path('budget-request/', views.BudgetRequestView.as_view(), name='budget_request'),
    path('budget-request/success/', views.budget_request_success, name='budget_request_success'),
    
    # Casos de Uso
    path('iot_industrial/', views.iot_industrial, name='iot_industrial'),
    path('iot_agriculture/', views.iot_agriculture, name='iot_agriculture')
]