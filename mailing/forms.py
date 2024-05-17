from django import forms

from mailing.models import Client, Mail, MailingSrv


class StyleFormMixin:
    """
    Миксин для добавления стилей к форме.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для модели Client с добавленными стилями.
    """

    class Meta:
        model = Client
        # fields = '__all__'
        exclude = ('owner',)


class MailForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для модели Mail с добавленными стилями.
    """

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        user = self.request.user
        super().__init__(*args, **kwargs)
        self.fields['mailings'].queryset = MailingSrv.objects.filter(owner=user)

    class Meta:
        model = Mail
        # fields = '__all__'
        exclude = ('owner',)


class MailingSrvForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для модели MailingSrv с добавленными стилями.
    """

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        user = self.request.user
        print(user)
        super().__init__(*args, **kwargs)
        self.fields['recipients'].queryset = Client.objects.filter(owner=user)
        self.fields['mail'].queryset = Mail.objects.filter(owner=user)

    class Meta:
        model = MailingSrv
        # fields = '__all__'
        exclude = ('owner',)


class ManagerMailingSrvForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для модели MailingSrv с добавленными стилями, для менеджера.
    """
    class Meta:
        model = MailingSrv
        fields = ('is_activated',)

class DeleteForm(forms.Form):
    """
    Форма для подтверждения удаления объекта.
    """
    confirm_delete = forms.BooleanField(label='Подтвердите удаление', required=True)
