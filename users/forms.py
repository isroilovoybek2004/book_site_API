from .models import CustomUser
from django.forms import Form,ModelForm
from django import forms


class CustomUserCreateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','password','email','image_user']


    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user


class CustomUserUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','image_user']