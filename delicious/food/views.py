# coding=utf-8
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
'''首页'''


class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {}

        context['topnav'] = 1

        return render_to_response('food-index.html', context, context_instance=RequestContext(request))