from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Item
# Create your views here.


class RequireLogin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RequireLogin, self).dispatch(*args, **kwargs)


class ItemList(generic.ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'manager/item_list.html'


class ItemDetail(generic.DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'manager/item_detail.html'


# Angular

class AngularIndex(RequireLogin, generic.TemplateView):
    template_name = 'manager/index.html'


class AngularMain(RequireLogin, generic.TemplateView):
    template_name = 'manager/angular_main.html'


class AngularDetail(RequireLogin, generic.TemplateView):
    template_name = 'manager/angular_detail.html'


class AngularNew(RequireLogin, generic.TemplateView):
    template_name = 'manager/angular_new.html'


# API Views
from rest_framework import generics
from .serializers import ItemSerializer
from rest_framework import permissions


class ItemApiList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        Return only objects created by user
        :return:
        """
        current_user = self.request.user
        return Item.objects.filter(user=current_user).order_by('-date_added')

    def pre_save(self, obj):
        obj.user = self.request.user


class ItemApiDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        Return only objects created by user
        :return:
        """
        current_user = self.request.user
        return Item.objects.filter(user=current_user)