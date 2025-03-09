from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ContactMessageForm, MeetingRequestForm, BudgetRequestForm
from .models import ContactMessage, MeetingRequest, BudgetRequest

def home(request):
    # Incluir o formulário de contacto na página inicial
    contact_form = ContactMessageForm()
    
    if request.method == 'POST':
        contact_form = ContactMessageForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'A sua mensagem foi enviada com sucesso! Entraremos em contacto brevemente.')
            return redirect('home')
    
    return render(request, 'home.html', {'contact_form': contact_form})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    contact_form = ContactMessageForm()
    
    if request.method == 'POST':
        contact_form = ContactMessageForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'A sua mensagem foi enviada com sucesso! Entraremos em contacto brevemente.')
            return redirect('contact')
    
    return render(request, 'contact.html', {'contact_form': contact_form})


class MeetingRequestView(CreateView):
    model = MeetingRequest
    form_class = MeetingRequestForm
    template_name = 'main/meeting_request.html'
    success_url = reverse_lazy('meeting_request_success')
    
    def form_valid(self, form):
        # Método chamado quando o formulário é válido
        messages.success(self.request, 'A sua solicitação de reunião foi enviada com sucesso! Entraremos em contacto para confirmar os detalhes.')
        return super().form_valid(form)


def meeting_request_success(request):
    return render(request, 'main/meeting_request_success.html')


class BudgetRequestView(CreateView):
    model = BudgetRequest
    form_class = BudgetRequestForm
    template_name = 'main/budget_request.html'
    success_url = reverse_lazy('budget_request_success')
    
    def form_valid(self, form):
        # Método chamado quando o formulário é válido
        messages.success(self.request, 'A sua solicitação de orçamento foi enviada com sucesso! Entraremos em contacto em breve.')
        return super().form_valid(form)


def budget_request_success(request):
    return render(request, 'main/budget_request_success.html')