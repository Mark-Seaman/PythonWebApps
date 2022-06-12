
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserAccount


# class AccountCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = UserAccount
#         fields = UserCreationForm.Meta.fields + ('bio',)


# class AccountChangeForm(UserChangeForm):

#     class Meta(UserChangeForm):
#         model = UserAccount
#         fields = UserChangeForm.Meta.fields
