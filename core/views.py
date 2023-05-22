from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from core import models, forms
from core.models import News


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


class NewsCreate(TitleMixin, CreateView):
    model = models.News
    template_name = 'core/news_create.html'
    context_object_name = 'news_create'
    form_class = forms.NewsForm
    success_url = reverse_lazy('core:home_page')
    title = "Добавление новости"


class NewsUpdate(TitleMixin, UpdateView):
    model = models.News
    template_name = 'core/news_update.html'
    context_object_name = 'news_update'
    form_class = forms.NewsForm
    success_url = reverse_lazy('core:home_page')
    title = "Редактирование новости"


class NewsDelete(TitleMixin, DeleteView):
    model = models.News
    template_name = 'core/news_delete.html'
    context_object_name = 'news_delete'
    success_url = reverse_lazy('core:home_page')
    title = "Удаление новости"


class DiscussionList(TitleMixin, ListView):
    model = models.Discussion
    template_name = 'core/discussion_page.html'
    context_object_name = 'discussion_page'
    title = 'Обсуждения'


class DiscussionCreate(TitleMixin, CreateView):
    model = models.Discussion
    template_name = 'core/discussion_create.html'
    context_object_name = 'discussion_create'
    form_class = forms.DiscussionForm
    success_url = reverse_lazy('core:discussion_page')
    title = "Добавление нового обсуждения"


class DiscussionDelete(TitleMixin, DeleteView):
    model = models.Discussion
    template_name = 'core/discussion_delete.html'
    context_object_name = 'discussion_delete'
    success_url = reverse_lazy('core:discussion_page')
    title = "Удаление обсуждения"
