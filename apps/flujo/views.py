from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from apps.flujo import models, forms


class ActivoCreateView(generic.CreateView):
    template_name = 'activo/form_activo.html'
    form_class = forms.FrmActivo
    model = models.Activo

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_activo')


class ActivoView(generic.ListView):
    template_name = 'activo/listar_activos.html'
    context_object_name = 'activos'
    model = models.Activo
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class Home(generic.TemplateView):
    template_name = 'home/login.html'