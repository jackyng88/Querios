from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.conf import settings


class IndexTemplateView(LoginRequiredMixin, TemplateView):
    """
    Class for the Index Template view
    The LoginRequiredMixin for when users access the REST API, doesn't show
    an empty page. Redirects to the login form. 
    """

    def get_template_names(self):
        # checking to see if in the settings.py file if the DEBUG attribute
        # is set to true or not. If true we use the index-dev.html template.
        if not settings.DEBUG:
            template_name = 'index-dev.html'
        else:
            template_name = 'index.html'
        return template_name
        