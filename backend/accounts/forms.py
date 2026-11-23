from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Name", max_length=150, widget=forms.TextInput(attrs={"placeholder": "Your name", "autocomplete": "given-name"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"placeholder": "you@example.com", "autocomplete": "email"}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = "Letters, digits and @/./+/-/_ only."
        self.fields["username"].widget.attrs.update(placeholder="dj_nickname", autocomplete="username")
        self.fields["password1"].help_text = "At least 8 characters, not only digits, not too common."
        self.fields["password1"].widget.attrs.update(autocomplete="new-password")
        self.fields["password2"].help_text = ""
        self.fields["password2"].widget.attrs.update(autocomplete="new-password")

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(placeholder="dj_nickname", autocomplete="username")
        self.fields["password"].widget.attrs.update(autocomplete="current-password")
