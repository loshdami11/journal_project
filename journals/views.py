from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Journal
from .forms import JournalForm


class JournalListView(ListView):
    """List of todos."""
    model = Journal
    template_name = 'journals/journal_list.html'
    context_object_name = 'journals'


class JournalDetailView(DetailView):
    "A journal."
    model = Journal
    template_name = 'journals/journal_detail.html'

class JournalCreateView(CreateView):
    """Create a journal."""
    model = Journal
    template_name = 'journals/journal_create.html'
    fields = '__all__'  
    success_url = reverse_lazy('home')  

class JournalUpdateView(UpdateView):
    """Update a journal"""
    model = Journal
    template_name = 'journals/journal_update.html'
    fields = ['title', 'daily_prompt', 'gratitude_section', 'goals', 'is_done']
    success_url = reverse_lazy('home')



class JournalDeleteView(DeleteView):
    """Delete a journal."""
    model = Journal
    template_name = 'journals/journal_delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journal'] = self.get_object()
        return context


