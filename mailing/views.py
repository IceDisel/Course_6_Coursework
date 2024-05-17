from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

from blog.models import BlogPost
from mailing.forms import ClientForm, DeleteForm, MailForm, MailingSrvForm, ManagerMailingSrvForm
from mailing.models import Client, Mail, MailingSrv


class IndexListView(TemplateView):
    """
    Контроллер для отображения страницы индекса.
    """
    template_name = 'mailing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Количество рассылок всего
        total_mailings = MailingSrv.objects.count()
        context['total_mailings'] = total_mailings

        # Количество активных рассылок
        active_mailings = MailingSrv.objects.filter(is_activated=True).count()
        context['active_mailings'] = active_mailings

        # Количество уникальных клиентов для рассылок
        unique_clients = Client.objects.values('email').distinct().count()
        context['unique_clients'] = unique_clients

        # Три случайные статьи из блога
        random_articles = BlogPost.objects.order_by('?')[:3]
        context['random_articles'] = random_articles

        return context


class ClientListView(LoginRequiredMixin, ListView):
    """
    Контроллер для отображения списка клиентов.
    """
    model = Client
    template_name = 'mailing/client_list.html'
    login_url = 'users:login'


class ClientDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра клиента.
    """
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания нового клиента.
    """
    model = Client
    form_class = ClientForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер для редактирования существующего клиента.
    """
    model = Client
    form_class = ClientForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления существующего клиента.
    """
    model = Client
    form_class = DeleteForm
    success_url = reverse_lazy('mailing:client_list')


class MailListView(LoginRequiredMixin, ListView):
    """
    Контроллер для отображения списка сообщений.
    """
    model = Mail
    login_url = 'users:login'


class MailDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра сообщения.
    """
    model = Mail


class MailCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания нового сообщения.
    """
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mailing:mail_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class MailUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер для редактирования существующего сообщения.
    """
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mailing:mail_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class MailDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления существующего сообщения.
    """
    model = Mail
    form_class = DeleteForm
    success_url = reverse_lazy('mailing:mail_list')


class MailingSrvListView(LoginRequiredMixin, ListView):
    """
    Контроллер для отображения списка рассылок.
    """
    model = MailingSrv
    login_url = 'users:login'


class MailingSrvDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра рассылки.
    """
    model = MailingSrv


class MailingSrvCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания новой рассылки.
    """
    model = MailingSrv
    form_class = MailingSrvForm
    success_url = reverse_lazy('mailing:mailingsrv_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class MailingSrvUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер для редактирования существующей рассылки.
    """
    model = MailingSrv
    form_class = MailingSrvForm
    success_url = reverse_lazy('mailing:mailingsrv_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class ManagerMailingSrvUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер для редактирования существующей рассылки.
    """
    model = MailingSrv
    form_class = ManagerMailingSrvForm
    success_url = reverse_lazy('mailing:mailingsrv_list')


class MailingSrvDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления существующей рассылки.
    """
    model = MailingSrv
    form_class = DeleteForm
    success_url = reverse_lazy('mailing:mailingsrv_list')
