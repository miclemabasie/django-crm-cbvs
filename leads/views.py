from email import message
from operator import sub
from django.core.mail import send_mail
from django.shortcuts import redirect, render, reverse
from .models import Lead, Agent
from .forms import LeadCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.views import LoginView
# Create your views here.

class LandingPageView(generic.TemplateView):
    template_name = 'landing_page.html'

    

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/leads_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'



class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/lead_detail.html'
    model = Lead
    queryset = Lead.objects.all()
    context_object_name = 'lead'
 
 
class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadCreateForm

    def get_success_url(self):
        return reverse('leads:lead_list')

    def form_valid(self, form):
        subject = 'Lead Created'
        message = 'You have successfuly created a lead'
        send_mail(subject=subject, message=message, from_email='crm@mail.com', recipient_list=['miclem@mail.com;'])
        return super(LeadCreateView, self).form_valid(form)
    

class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadCreateForm
    
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')


class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')

    
