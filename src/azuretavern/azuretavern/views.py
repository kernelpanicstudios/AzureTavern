"""Site-wide views for the Azure Tavern."""

from django.core import urlresolvers
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import FormView, RedirectView, TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    success_url = urlresolvers.reverse_lazy('home')

    def form_valid(self, form):
        login(self.request, form.user_cache)
        return super(LoginView, self).form_valid(form)

class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = urlresolvers.reverse_lazy('registration_complete')

class RegistrationCompleteView(TemplateView):
    template_name = 'accounts/complete.html'

class LogoutView(RedirectView):
    pattern_name = 'home'

    def get(self, request, *args, **kwargs):
        """Logs the user out."""
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
