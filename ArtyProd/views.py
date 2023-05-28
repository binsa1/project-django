from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import About, Service, RecentWork, Team
from django.shortcuts import render, redirect

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        context['team'] = Team.objects.all()
        return context

def login_view(request):
 return render(request, 'login.html')

