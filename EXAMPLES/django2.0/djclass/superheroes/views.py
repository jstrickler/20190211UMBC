from django.views.generic import (
    TemplateView, ListView, CreateView, DetailView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Superhero, City




def view_details(request):
    # get object
    # pass object to template
    # REurn rendered template
    pass

@login_required
def home(request):
    x = request.session.get('color', None)
    request.session['color'] = 'mauve'
    data = {
        'message': 'Welcome to the superheroes app for class-based views',
    }
    return render(request, 'home.html', data)


class GenericContext(TemplateView):
    message = 'with context'
    fruits = ['apple', 'banana', 'lemon']
    template_name ='generic_context.html'
    # cannot access self.request HERE

    # def get(self):
    #     super().get()

    def spam(self):
        x = self.request.session.get('animal', 'wildebeest')
        self.request.session['animal'] = 'wombat'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'message': self.message,
                'fruits': self.fruits
            }
        )
        return context


class HeroDetailViewMinimal(DetailView):
    model = Superhero


class HeroListViewMinimal(ListView):
    model = Superhero

class HeroListView(ListView):
    context_object_name = 'heroes'
    template_name = 'hero_list.html'
    model = Superhero


class HeroDetailView(DetailView):
    context_object_name = 'hero'
    template_name = 'superhero_details.html'
    model = Superhero

# class CreateViewBase(CreateView):
#     success_url = reverse_lazy('superheroes:success')


class CityCreateView(CreateView):
    model = City
    fields = ['name']
    success_url = reverse_lazy('superheroes:success')
    # form_name = 'superhero_form.html'

class HeroCreateView(CreateView):
    model = Superhero
    # template = "hero_create.html"
    fields = ['name', 'real_name', 'secret_identity', 'city']
    success_url = reverse_lazy('superheroes:success')
    # form_class = MyCoolForm

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    model = Superhero
    # template = "hero_update.html"
    fields = ['name', 'real_name', 'secret_identity', 'city']
    success_url = reverse_lazy('superheroes:success')

class SuccessView(TemplateView):
    template_name = 'success.html'

class Table(ListView):
    template_name = 'table.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['heading'] = self.model.__name__
        return data

class HeroTable(Table):
    model = Superhero
    template_name = 'hero_table.html'


