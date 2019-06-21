from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class IndexTemplateView(LoginRequiredMixin, TemplateView):
    """
    Class for the Index Template view
    The LoginRequiredMixin for when users access the REST API, doesn't show
    an empty page. Redirects to the login form. 
    """

    def get_template_names(self):
        # Overriding the get_template_names method.
        template_name = 'index.html'
        return template_name
        