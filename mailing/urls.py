from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import IndexListView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    ClientDetailView, MailListView, MailCreateView, MailUpdateView, MailDeleteView, MailDetailView, MailingSrvListView, \
    MailingSrvCreateView, MailingSrvUpdateView, MailingSrvDeleteView, MailingSrvDetailView, ManagerMailingSrvUpdateView

app_name = MailingConfig.name

urlpatterns = [
    path('', cache_page(60)(IndexListView.as_view()), name='index'),

    path('client_list', ClientListView.as_view(), name='client_list'),
    path('client_detail/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('add_client', ClientCreateView.as_view(), name='add_client'),
    path('edit_client/<int:pk>', ClientUpdateView.as_view(), name='edit_client'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),

    path('mail_list', MailListView.as_view(), name='mail_list'),
    path('mail_detail/<int:pk>', MailDetailView.as_view(), name='mail_detail'),
    path('add_mail', MailCreateView.as_view(), name='add_mail'),
    path('edit_mail/<int:pk>', MailUpdateView.as_view(), name='edit_mail'),
    path('delete_mail/<int:pk>', MailDeleteView.as_view(), name='delete_mail'),

    path('mailingsrv_list', MailingSrvListView.as_view(), name='mailingsrv_list'),
    path('mailingsrv_detail/<int:pk>', MailingSrvDetailView.as_view(), name='mailingsrv_detail'),
    path('add_mailingsrv', MailingSrvCreateView.as_view(), name='add_mailingsrv'),
    path('edit_mailingsrv/<int:pk>', MailingSrvUpdateView.as_view(), name='edit_mailingsrv'),
    path('edit_manager_mailingsrv/<int:pk>', ManagerMailingSrvUpdateView.as_view(), name='edit_manager_mailingsrv'),
    path('delete_mailingsrv/<int:pk>', MailingSrvDeleteView.as_view(), name='delete_mailingsrv'),

]
