from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.core.mail import send_mail
import os

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в магазин техники "ТехноМир"'
        message = 'Спасибо, Вы успешно зарегистрировались!'
        from_email = os.getenv('EMAIL_HOST_USER')
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)
