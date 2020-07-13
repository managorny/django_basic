from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authapp.forms import forms
from authapp.models import ShopUser


class AdminShopUserCreateForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = (
            'username', 'first_name', 'last_name', 'is_superuser',
            'password1', 'password2', 'email', 'age', 'avatar'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Пользователь слишком молод!")
        return data


class AdminShopUserUpdateForm(UserChangeForm):
    class Meta:
        model = ShopUser
        # fields = '__all__'
        fields = (
            'username', 'first_name', 'last_name', 'is_superuser',
            'password', 'email', 'age', 'avatar', 'is_active', 'is_staff'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget = forms.HiddenInput()
            else:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Пользователь слишком молод!")
        return data
