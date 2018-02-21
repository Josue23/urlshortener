from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import KirrURL
# from . import View


def kirr_redirect_view(request, shortcode=None, *args, **kwargs): # function based view
    # print(request.user.is_authenticated())
    # print(shortcode)
    print('Method is')
    print(request.method)
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    # obj_url = obj.url

    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()

    # obj_url = None
    # qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url

    return HttpResponse('Hello {sc}'.format(sc=obj.url))


class KirrCBView(View): # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        # print(request.user.is_authenticated())
        # print(shortcode)
        return HttpResponse('Hello again {sc}'.format(sc=shortcode))
    
    def post(self, request, *args, **kwargs):
        return HttpResponse()