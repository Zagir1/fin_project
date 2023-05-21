from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('home_page/', views.NewsList.as_view(), name='home_page'),
    path('news_detail/<int:pk>', views.NewsDetail.as_view(), name='news_detail'),
    path('news_create/', views.NewsCreate.as_view(), name='news_create'),
    path('news_update/<int:pk>', views.NewsUpdate.as_view(), name='news_update'),
    path('news_delete/<int:pk>', views.NewsDelete.as_view(), name='news_delete'),
    path('discussion_page/', views.DiscussionList.as_view(), name='discussion_page'),
    path('discussion_create/', views.DiscussionCreate.as_view(), name='discussion_create'),
    path('discussion_delete/<int:pk>', views.DiscussionDelete.as_view(), name='discussion_delete'),
]
