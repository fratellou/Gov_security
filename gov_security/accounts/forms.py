from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'autofocus': True}),
        error_messages={
            'required': 'Пожалуйста, введите корректное имя пользователя'}
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Пожалуйста, введите корректный пароль'}
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        errors = []
        if not username:
            errors.append(forms.ValidationError(
                'Пожалуйста, введите имя пользователя.'))
        if not password:
            errors.append(forms.ValidationError('Пожалуйста, введите пароль.'))
        if errors:
            raise ValidationError(errors)
        return super().clean()
