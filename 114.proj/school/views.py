from typing import Any, Optional
from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView

# Create your views here.
class CodeRedirectView(RedirectView):
    url = "https://www.google.com/"

# class GeekRedirectView(RedirectView):
#     url = '/'

class GeekRedirectView(RedirectView):
    pattern_name = 'minindex'
    # now status code will be 301 that is permanent redirect
    permanent = False
    # now query string is visible in URL, by default it is not visible
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        '''You can construct url ''' 
        print("args: ",args)
        print("kwargs: ",kwargs)
        return super().get_redirect_url(*args,**kwargs)