from django.contrib import admin

from mailing.models import Client, MailingSrv, Log


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email', 'owner', 'comment',)
    list_filter = ('owner',)
    search_fields = ('email',)


@admin.register(MailingSrv)
class MailingSrvAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'start', 'finish', 'status', 'frequency',)


@admin.register(Log)
class AdminLog(admin.ModelAdmin):
    list_display = ('attempt_time', 'status', 'server_response', 'mailing',)
