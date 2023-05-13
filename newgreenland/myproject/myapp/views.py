import datetime

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum,Count,F
from django.http import HttpResponse
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from .forms import *
from .models import *

class Test(View):
    def get(self,request):
        return render(request, 'base.html')