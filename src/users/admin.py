from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ('email', 'last_name', 'first_name', 'is_staff', 'is_active', 'date_joined', 'last_login',)
    list_filter = ('is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('id',)

    fieldsets = (
        ('СОТРУДНИК', {'fields': ('last_name', 'first_name', 'surname')}),
        ('УЧЕТНАЯ ЗАПИСЬ', {'fields': ('email', 'password', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'is_staff', 'is_active')}
         ),
    )

    def save_model(self, request, obj, form, change):
        if not change and (not form.cleaned_data['password1'] or not obj.has_usable_password()):
            password = get_random_string(length=12)
            obj.set_password(password)
            send_mail(
                subject='Ростелеком Бизнес',
                message='Вы зарегистрированы в системе отслеживания пути заявок на подключение клиентов\n'
                        f'Ваш логин - {obj.email}, пароль - {password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[obj.email]
            )

        super().save_model(request, obj, form, change)


admin.site.unregister(Group)
