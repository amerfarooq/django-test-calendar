from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser

    def clean_username(self):
        username = self.cleaned_data['username']
        
        try:
            MyUser.objects.get(username=username)
        except MyUser.DoesNotExist:
            return username
        raise forms.ValidationError("Username already exists!")


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('userType',)}),
    )

admin.site.register(MyUser, MyUserAdmin)