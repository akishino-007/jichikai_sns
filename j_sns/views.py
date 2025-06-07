from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    DeleteView,
    UpdateView,
)
from django.core.paginator import Paginator

from .models import Info, Review
from .consts import ITEM_PER_PAGE


# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('index')


class ListJSnsView(LoginRequiredMixin, ListView):
    template_name = 'j_sns/j_sns_list.html'
    model = Info
    paginate_by = ITEM_PER_PAGE

class ListJSnskairanView(LoginRequiredMixin, ListView):
    template_name = 'j_sns/j_sns_kairan_list.html'
    model = Info
    paginate_by = ITEM_PER_PAGE

class ListJSnskeijibanView(LoginRequiredMixin, ListView):
    template_name = 'j_sns/j_sns_keijiban_list.html'
    model = Info
    paginate_by = ITEM_PER_PAGE

class ListJSnsosiraseView(LoginRequiredMixin, ListView):
    template_name = 'j_sns/j_sns_osirase_list.html'
    model = Info
    paginate_by = ITEM_PER_PAGE

class DetailJSnsView(LoginRequiredMixin, DetailView):
    template_name = 'j_sns/j_sns_detail.html'
    model = Info

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(title=self.object)  # Review のデータを明示的に渡す
        print(context)
        return context


class CreateJSnsView(LoginRequiredMixin, CreateView):
    template_name = 'j_sns/j_sns_create.html'
    model = Info
    fields = ('category','title','content', 'thumbnail1', 'thumbnail2', 'thumbnail3')
    success_url = reverse_lazy('list-jsns')

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)

class DeleteJSnsView(LoginRequiredMixin, DeleteView):
    template_name = 'j_sns/j_sns_confirm_delete.html'
    model = Info
    success_url = reverse_lazy('list-jsns')

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj

class UpdateJSnsView(LoginRequiredMixin, UpdateView):
    model = Info
    fields = ('category','title','content', 'thumbnail1', 'thumbnail2', 'thumbnail3')
    template_name = 'j_sns/j_sns_update.html'
    success_url = reverse_lazy('list-jsns')

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj
    
    def get_success_url(self):
        return reverse('detail-jsns', kwargs={'pk':self.object.id})

def index_view(request):
    object_list = Info.objects.all()
    paginator = Paginator(object_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page',1)
    page_obj = paginator.page(page_number)
    return render(request, 'j_sns/index.html', {'page_obj': page_obj},)

class CreateReviewView(CreateView):
    model = Review
    fields = ('text', 'title')
    template_name = 'j_sns/review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['j_sns'] = Info.objects.get(pk=self.kwargs['j_sns_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.title = Info.objects.get(pk=self.kwargs['j_sns_id'])  # title を明示的に設定
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('detail-jsns', kwargs={'pk': self.object.title.id})