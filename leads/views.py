from re import template
from django.shortcuts import redirect, render, reverse
from .models import Lead, Agent
from .forms import LeadCreateForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

class LandingPageView(TemplateView):
    template_name = 'landing_page.html'


class LeadListView(ListView):
    template_name = 'leads/leads_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(DetailView):
    template_name = 'leads/lead_detail.html'
    model = Lead
    queryset = Lead.objects.all()
    context_object_name = 'lead'
 
 
class LeadCreateView(CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadCreateForm

    def get_success_url(self):
        return reverse('leads:lead_list')
    

class LeadUpdateView(UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadCreateForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')


class LeadDeleteView(DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')