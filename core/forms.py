from django import forms
from django.forms import ModelForm
from core.models import News, Discussion, Section, Author, User


class NewsForm(ModelForm):
    title = forms.CharField(label="Название новости", required=True)
    topic = forms.ModelMultipleChoiceField(label="Раздел(ы) новости", queryset=Section.objects.all())
    summary = forms.CharField(widget=forms.Textarea, label="Информация для новости", required=True)
    picture = forms.FileField(label="Картинка для новости", required=False)
    auth_opinion = forms.CharField(widget=forms.Textarea, label="Мнение автора новости", required=False)
    author = forms.ModelChoiceField(label="Автор новости", queryset=Author.objects.all())
    source = forms.URLField(label="Источник новости", required=False)
    d_created = forms.DateTimeField(label="Дата и время публикации", required=True)
    active = forms.BooleanField(label="Активна ли новость?")

    def clean_title(self):
        name = self.cleaned_data['title']
        if name.isdigit():
            raise forms.ValidationError('Название не должно являться числом!')
        return name

    class Meta:
        model = News
        fields = "__all__"


class DiscussionForm(ModelForm):
    username = forms.ModelChoiceField(label="Имя пользователя", queryset=User.objects.all())
    topic = forms.ModelMultipleChoiceField(label="Раздел(ы) обсуждения", queryset=Section.objects.all())
    d_title = forms.CharField(label="Название обсуждения", required=False)
    branch = forms.CharField(widget=forms.Textarea, label="Изложение сути вопроса", required=False)
    picture = forms.FileField(label="Картинка для обсуждения", required=False)

    class Meta:
        model = Discussion
        fields = "__all__"
