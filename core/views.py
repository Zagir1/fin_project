from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from core import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


class NewsList(TitleMixin, ListView):
    model = models.News
    template_name = 'core/home_page.html'
    context_object_name = 'news'
    title = 'Wingman'


class NewsDetail(TitleMixin, DetailView):
    model = models.News
    template_name = 'core/news_detail.html'
    context_object_name = 'news_detail'
    title = "Новость"


class NewsCreate(TitleMixin, LoginRequiredMixin, CreateView):
    model = models.News
    template_name = 'core/news_create.html'
    context_object_name = 'news_create'
    form_class = forms.NewsForm
    success_url = reverse_lazy('core:home_page')
    title = "Добавление новости"


class NewsUpdate(TitleMixin, LoginRequiredMixin, UpdateView):
    model = models.News
    template_name = 'core/news_update.html'
    context_object_name = 'news_update'
    form_class = forms.NewsForm
    success_url = reverse_lazy('core:home_page')
    title = "Редактирование новости"

#    def form_valid(self, form):
#        messages.success(self.request, "Новость была обновлена успешно")
#        return super(NewsUpdate, self).form_valid(form)

#    def get_queryset(self):
#        base_qs = super(NewsUpdate, self).get_queryset()
#        return base_qs.filter(superuser=self.request.superuser)


class NewsDelete(TitleMixin, LoginRequiredMixin, DeleteView):
    model = models.News
    template_name = 'core/news_delete.html'
    context_object_name = 'news_delete'
    success_url = reverse_lazy('core:home_page')
    title = "Удаление новости"

#    def form_valid(self, form):
#        messages.success(self.request, "Новость была удалена успешно")
#        return super(NewsDelete, self).form_valid(form)

#    def get_queryset(self):
#        base_qs = super(NewsDelete, self).get_queryset()
#        return base_qs.filter(user=self.request.user)


class DiscussionList(TitleMixin, ListView):
    model = models.Discussion
    template_name = 'core/discussion_page.html'
    context_object_name = 'discussion_page'
    title = 'Обсуждения'


class DiscussionCreate(TitleMixin, LoginRequiredMixin, CreateView):
    model = models.Discussion
    template_name = 'core/discussion_create.html'
    context_object_name = 'discussion_create'
    form_class = forms.DiscussionForm
    success_url = reverse_lazy('core:discussion_page')
    title = "Добавление нового обсуждения"


class DiscussionDelete(TitleMixin, LoginRequiredMixin, DeleteView):
    model = models.Discussion
    template_name = 'core/discussion_delete.html'
    context_object_name = 'discussion_delete'
    success_url = reverse_lazy('core:discussion_page')
    title = "Удаление обсуждения"

#    def form_valid(self, form):
#        messages.success(self.request, "Обсуждение было удалено успешно")
#        return super(DiscussionDelete, self).form_valid(form)

#    def get_queryset(self):
#        base_qs = super(DiscussionDelete, self).get_queryset()
#        return base_qs.filter(superuser=self.request.superuser)
