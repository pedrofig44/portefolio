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
    path('use-cases/', views.use_cases_menu, name='use_cases_menu'),
    path('iot_industrial/', views.iot_industrial, name='iot_industrial'),
    path('iot_agriculture/', views.iot_agriculture, name='iot_agriculture'),
    path('iot_smart_cities/', views.iot_smart_cities, name='iot_smart_cities'),
    path('automation/', views.automation, name='automation'),
    
    # Legal Pages
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('cookie-policy/', views.cookie_policy, name='cookie_policy'),
]