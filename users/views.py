import random
import string

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, UpdateView

from users.forms import UserRegisterForm, UserUpdateForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация пользователя'
        return context

    def get_success_url(self):
        return reverse_lazy('mailing:index')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False

        current_site = self.request.get_host()

        subject = 'Подтверждение регистрации'

        verification_code = ''.join(str(random.randint(1, 9)) for _ in range(9))
        user.verification_code = verification_code

        message = (f"Вы успешно зарегестрировались на нашем сайте. Чтобы продолжить пользоваться ресурсом необходимо"
                   f"подтвердить регистрацию по ссылке http://{current_site}/confirm/ и ввести код {verification_code}")

        user.save()

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email, ],

        )

        user.save()

        return super().form_valid(form)


class ConfirmRegistrationUserView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/confirm_registration_user.html')

    def post(self, request, *args, **kwargs):
        verification_code = request.POST.get('verification_code')

        user = get_object_or_404(User, verification_code=verification_code)

        if user:
            user.is_active = True
            user.save()

            return redirect('users:login')
        return redirect('mailing:index')


class CustomPasswordResetView(TemplateView):
    model = User
    template_name = 'users/reset_password.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        user = User.objects.get(email=email)

        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        user.password = make_password(new_password)
        user.save()

        send_mail(
            subject='Восстановление пароля',
            message='Ваш новый пароль: {}'.format(new_password),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )

        return HttpResponseRedirect('confirm/')


class PasswordRecoveryMessageView(TemplateView):
    template_name = 'users/password_recovery_message.html'


class UserListView(UserPassesTestMixin, ListView):
    model = User
    template_name = 'users/user_list.html'  # замените на ваш шаблон

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists() or self.request.user.is_superuser


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:list_users')
