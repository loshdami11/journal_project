from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Journal
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin




class JournalListView(ListView):
    """List of todos."""
    model = Journal
    template_name = 'journals/journal_list.html'
    context_object_name = 'journals'


class JournalDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    "A journal."
    model = Journal
    template_name = 'journals/journal_detail.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

class JournalCreateView(LoginRequiredMixin,CreateView):
    """Create a journal."""
    model = Journal
    template_name = 'journals/journal_create.html'
    fields = '__all__'  
    success_url = reverse_lazy('home')  
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JournalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update a journal"""
    model = Journal
    template_name = 'journals/journal_update.html'
    fields = ['title', 'daily_prompt', 'gratitude_section', 'goals', 'is_done']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class JournalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a journal."""
    model = Journal
    template_name = 'journals/journal_delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journal'] = self.get_object()
        return context
    
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


